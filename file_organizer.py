"""
File Organizer - Handles file classification and movement
No OOP patterns used - functional approach
"""

import os
import shutil

# File categories and their extensions
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp'],
    'Videos': ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv', '.webm', '.m4v'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.pages'],
    'Spreadsheets': ['.xls', '.xlsx', '.csv', '.ods', '.numbers'],
    'Presentations': ['.ppt', '.pptx', '.key', '.odp'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
    'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.php', '.rb', '.go'],
    'Executables': ['.exe', '.msi', '.app', '.dmg', '.deb', '.rpm'],
    'Others': []
}

def categorize_file(filename):
    """Categorize a file based on its extension"""
    file_ext = os.path.splitext(filename)[1].lower()
    
    for category, extensions in FILE_CATEGORIES.items():
        if file_ext in extensions:
            return category
    
    # If no category matches, put in "Others"
    return "Others"

def get_unique_filename(filepath):
    """Generate a unique filename if the destination already exists"""
    if not os.path.exists(filepath):
        return filepath
    
    name, ext = os.path.splitext(filepath)
    counter = 1
    
    while os.path.exists(f"{name}_{counter}{ext}"):
        counter += 1
    
    return f"{name}_{counter}{ext}"

def move_file_to_category(source_path, destination_path):
    """Move a file to its category folder with error handling"""
    try:
        # Handle duplicate filenames
        destination_path = get_unique_filename(destination_path)
        
        # Create destination directory if it doesn't exist
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)
        
        # Move the file
        shutil.move(source_path, destination_path)
        return True, os.path.basename(destination_path)
        
    except Exception as e:
        return False, str(e)

def get_files_in_folder(folder_path):
    """Get all files in the specified folder"""
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Folder not found: {folder_path}")
    
    files = []
    try:
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isfile(item_path):
                files.append(item)
    except PermissionError:
        raise PermissionError(f"Permission denied accessing folder: {folder_path}")
    
    return files

def organize_folder(folder_path):
    """Organize files in the specified folder by type"""
    # Validate folder path
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Folder not found: {folder_path}")
    
    if not os.path.isdir(folder_path):
        raise NotADirectoryError(f"Path is not a directory: {folder_path}")
    
    # Initialize organized files dictionary
    organized_files = {category: [] for category in FILE_CATEGORIES.keys()}
    
    # Get all files in the folder
    files = get_files_in_folder(folder_path)
    
    if not files:
        return organized_files  # Return empty categories if no files found
    
    # Process each file
    for filename in files:
        file_path = os.path.join(folder_path, filename)
        category = categorize_file(filename)
        
        if category:
            # Create category folder path
            category_path = os.path.join(folder_path, category)
            destination = os.path.join(category_path, filename)
            
            # Move file to category folder
            success, result = move_file_to_category(file_path, destination)
            
            if success:
                organized_files[category].append(result)
            else:
                raise Exception(f"Failed to move {filename}: {result}")
    
    return organized_files

def get_category_stats(organized_files):
    """Get statistics about organized files"""
    stats = {}
    total_files = 0
    
    for category, files in organized_files.items():
        file_count = len(files)
        stats[category] = file_count
        total_files += file_count
    
    stats['total'] = total_files
    return stats

def validate_file_operation(file_path):
    """Validate if a file operation is safe to perform"""
    if not os.path.exists(file_path):
        return False, "File does not exist"
    
    if not os.path.isfile(file_path):
        return False, "Path is not a file"
    
    try:
        # Check if file is accessible
        with open(file_path, 'rb') as f:
            pass
        return True, "File is accessible"
    except PermissionError:
        return False, "Permission denied"
    except OSError as e:
        return False, f"OS Error: {str(e)}"

def get_file_size(file_path):
    """Get file size in bytes"""
    try:
        return os.path.getsize(file_path)
    except OSError:
        return 0

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

def get_total_folder_size(folder_path):
    """Calculate total size of all files in a folder"""
    total_size = 0
    
    try:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                total_size += get_file_size(file_path)
    except OSError:
        pass
    
    return total_size

def is_safe_to_organize(folder_path):
    """Check if it's safe to organize the folder"""
    if not os.path.exists(folder_path):
        return False, "Folder does not exist"
    
    if not os.path.isdir(folder_path):
        return False, "Path is not a directory"
    
    try:
        # Check if we can read the directory
        os.listdir(folder_path)
        return True, "Folder is accessible"
    except PermissionError:
        return False, "Permission denied accessing folder"
    except OSError as e:
        return False, f"OS Error: {str(e)}" 