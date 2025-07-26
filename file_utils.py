"""
File Utils - Helper functions for file operations
No OOP patterns used - functional approach
"""

import os
import shutil
from datetime import datetime
from pathlib import Path

def get_file_extension(filename):
    """Get the file extension in lowercase"""
    return os.path.splitext(filename)[1].lower()

def is_hidden_file(filename):
    """Check if a file is hidden (starts with dot on Unix or has hidden attribute on Windows)"""
    return filename.startswith('.') or has_hidden_attribute(filename)

def has_hidden_attribute(filepath):
    """Check if a file has the hidden attribute (Windows)"""
    try:
        import stat
        return bool(os.stat(filepath).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)
    except (AttributeError, OSError):
        return False

def get_file_info(filepath):
    """Get comprehensive information about a file"""
    try:
        stat_info = os.stat(filepath)
        return {
            'size': stat_info.st_size,
            'created': datetime.fromtimestamp(stat_info.st_ctime),
            'modified': datetime.fromtimestamp(stat_info.st_mtime),
            'accessed': datetime.fromtimestamp(stat_info.st_atime),
            'is_file': os.path.isfile(filepath),
            'is_dir': os.path.isdir(filepath),
            'exists': True
        }
    except OSError:
        return {
            'size': 0,
            'created': None,
            'modified': None,
            'accessed': None,
            'is_file': False,
            'is_dir': False,
            'exists': False
        }

def format_file_size(size_bytes):
    """Format file size in human-readable format"""
    if size_bytes == 0:
        return "0 B"
    
    size_names = ["B", "KB", "MB", "GB", "TB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    
    return f"{size_bytes:.1f} {size_names[i]}"

def is_safe_to_move(filepath):
    """Check if it's safe to move a file"""
    if not os.path.exists(filepath):
        return False, "File does not exist"
    
    if not os.path.isfile(filepath):
        return False, "Path is not a file"
    
    try:
        # Check if file is not in use by trying to open it
        with open(filepath, 'rb') as f:
            pass
        return True, "File is accessible"
    except PermissionError:
        return False, "Permission denied"
    except OSError as e:
        return False, f"OS Error: {str(e)}"

def get_unique_filename(filepath):
    """Generate a unique filename if the destination already exists"""
    if not os.path.exists(filepath):
        return filepath
    
    name, ext = os.path.splitext(filepath)
    counter = 1
    
    while os.path.exists(f"{name}_{counter}{ext}"):
        counter += 1
    
    return f"{name}_{counter}{ext}"

def safe_move_file(source, destination):
    """Safely move a file with error handling"""
    try:
        # Check if source exists and is accessible
        safe, message = is_safe_to_move(source)
        if not safe:
            return False, f"Cannot access source file: {message}"
        
        # Create destination directory if it doesn't exist
        dest_dir = os.path.dirname(destination)
        if dest_dir and not os.path.exists(dest_dir):
            os.makedirs(dest_dir, exist_ok=True)
        
        # Handle duplicate filenames
        destination = get_unique_filename(destination)
        
        # Move the file
        shutil.move(source, destination)
        return True, os.path.basename(destination)
        
    except Exception as e:
        return False, str(e)

def get_directory_size(directory_path):
    """Calculate total size of a directory and all its contents"""
    total_size = 0
    file_count = 0
    dir_count = 0
    
    try:
        for root, dirs, files in os.walk(directory_path):
            dir_count += len(dirs)
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    total_size += os.path.getsize(file_path)
                    file_count += 1
                except OSError:
                    continue
    except OSError:
        pass
    
    return {
        'size': total_size,
        'size_formatted': format_file_size(total_size),
        'file_count': file_count,
        'dir_count': dir_count
    }

def count_files_by_extension(directory_path):
    """Count files by their extensions in a directory"""
    extension_counts = {}
    
    try:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                ext = get_file_extension(file)
                extension_counts[ext] = extension_counts.get(ext, 0) + 1
    except OSError:
        pass
    
    return extension_counts

def get_oldest_and_newest_files(directory_path):
    """Find the oldest and newest files in a directory"""
    oldest_file = None
    newest_file = None
    oldest_time = float('inf')
    newest_time = 0
    
    try:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    mtime = os.path.getmtime(file_path)
                    if mtime < oldest_time:
                        oldest_time = mtime
                        oldest_file = file_path
                    if mtime > newest_time:
                        newest_time = mtime
                        newest_file = file_path
                except OSError:
                    continue
    except OSError:
        pass
    
    return {
        'oldest': oldest_file,
        'newest': newest_file,
        'oldest_time': datetime.fromtimestamp(oldest_time) if oldest_file else None,
        'newest_time': datetime.fromtimestamp(newest_time) if newest_file else None
    }

def validate_directory_access(directory_path):
    """Validate if a directory can be accessed and modified"""
    if not os.path.exists(directory_path):
        return False, "Directory does not exist"
    
    if not os.path.isdir(directory_path):
        return False, "Path is not a directory"
    
    try:
        # Test read access
        os.listdir(directory_path)
    except PermissionError:
        return False, "Permission denied - cannot read directory"
    except OSError as e:
        return False, f"OS Error reading directory: {str(e)}"
    
    try:
        # Test write access
        test_file = os.path.join(directory_path, "test_write.tmp")
        with open(test_file, 'w') as f:
            f.write("test")
        os.remove(test_file)
    except PermissionError:
        return False, "Permission denied - cannot write to directory"
    except OSError as e:
        return False, f"OS Error writing to directory: {str(e)}"
    
    return True, "Directory is accessible and writable"

def create_backup_list(organized_files):
    """Create a list of files that were organized for potential backup"""
    backup_list = []
    
    for category, files in organized_files.items():
        if files:
            for filename in files:
                backup_list.append({
                    'filename': filename,
                    'category': category,
                    'original_path': None  # Would be set if tracking original locations
                })
    
    return backup_list

def estimate_organization_time(file_count):
    """Estimate the time needed to organize files based on count"""
    # Rough estimation: 0.1 seconds per file + 0.5 seconds overhead
    estimated_seconds = (file_count * 0.1) + 0.5
    
    if estimated_seconds < 60:
        return f"{estimated_seconds:.1f} seconds"
    elif estimated_seconds < 3600:
        minutes = estimated_seconds / 60
        return f"{minutes:.1f} minutes"
    else:
        hours = estimated_seconds / 3600
        return f"{hours:.1f} hours"

def get_system_info():
    """Get basic system information for logging"""
    import platform
    import sys
    
    return {
        'platform': platform.system(),
        'platform_version': platform.version(),
        'python_version': sys.version,
        'architecture': platform.architecture()[0]
    } 