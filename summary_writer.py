"""
Summary Writer - Generates detailed summary reports for organized folders
No OOP patterns used - functional approach
"""

import os
from datetime import datetime

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

def get_file_info(file_path):
    """Get detailed information about a file"""
    try:
        file_size = os.path.getsize(file_path)
        file_stat = os.stat(file_path)
        
        return {
            'size': file_size,
            'size_formatted': format_file_size(file_size),
            'created': datetime.fromtimestamp(file_stat.st_ctime),
            'modified': datetime.fromtimestamp(file_stat.st_mtime),
            'accessed': datetime.fromtimestamp(file_stat.st_atime)
        }
    except OSError:
        return {
            'size': 0,
            'size_formatted': 'Unknown',
            'created': None,
            'modified': None,
            'accessed': None
        }

def create_summary_header(category, timestamp, file_count):
    """Create the header section of a summary file"""
    header = []
    header.append(f"📁 {category} - File Summary")
    header.append("=" * 50)
    header.append(f"Generated on: {timestamp}")
    header.append(f"Total files: {file_count}")
    header.append("=" * 50)
    header.append("")
    
    return "\n".join(header)

def create_file_listing(files, category_path):
    """Create a formatted list of files with details"""
    file_list = []
    
    for i, filename in enumerate(files, 1):
        file_path = os.path.join(category_path, filename)
        file_info = get_file_info(file_path)
        
        # Format the file entry
        file_entry = f"{i:3d}. {filename:<40} ({file_info['size_formatted']})"
        file_list.append(file_entry)
    
    return "\n".join(file_list)

def create_summary_footer():
    """Create the footer section of a summary file"""
    footer = []
    footer.append("")
    footer.append("=" * 50)
    footer.append("End of summary")
    
    return "\n".join(footer)

def write_summary_file(summary_path, content):
    """Write content to a summary file with proper encoding"""
    try:
        with open(summary_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"Error writing summary file: {e}")
        return False

def generate_category_summary(category, files, base_folder, timestamp):
    """Generate a summary for a specific category"""
    if not files:
        return None  # No files to summarize
    
    category_path = os.path.join(base_folder, category)
    summary_path = os.path.join(category_path, "summary.txt")
    
    # Create summary content
    header = create_summary_header(category, timestamp, len(files))
    file_list = create_file_listing(files, category_path)
    footer = create_summary_footer()
    
    # Combine all sections
    summary_content = f"{header}{file_list}\n{footer}"
    
    # Write the summary file
    success = write_summary_file(summary_path, summary_content)
    
    return success

def generate_summaries(base_folder, organized_files):
    """Generate summary files for each category folder"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    summary_results = {}
    
    for category, files in organized_files.items():
        if files:
            success = generate_category_summary(category, files, base_folder, timestamp)
            summary_results[category] = success
        else:
            summary_results[category] = None  # No files to summarize
    
    return summary_results

def create_master_summary(base_folder, organized_files):
    """Create a master summary file in the base folder"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    master_summary_path = os.path.join(base_folder, "MASTER_SUMMARY.txt")
    
    # Calculate totals
    total_files = sum(len(files) for files in organized_files.values())
    total_categories = sum(1 for files in organized_files.values() if files)
    
    # Create master summary content
    content = []
    content.append("📁 MASTER SUMMARY - Folder Organization Report")
    content.append("=" * 60)
    content.append(f"Generated on: {timestamp}")
    content.append(f"Base folder: {base_folder}")
    content.append(f"Total files organized: {total_files}")
    content.append(f"Categories created: {total_categories}")
    content.append("=" * 60)
    content.append("")
    
    # Add category breakdown
    content.append("📊 Category Breakdown:")
    content.append("-" * 30)
    
    for category, files in organized_files.items():
        if files:
            content.append(f"📁 {category}: {len(files)} files")
    
    content.append("")
    content.append("=" * 60)
    content.append("End of master summary")
    
    # Write master summary
    master_content = "\n".join(content)
    return write_summary_file(master_summary_path, master_content)

def create_detailed_report(base_folder, organized_files):
    """Create a detailed report with file statistics"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_path = os.path.join(base_folder, "DETAILED_REPORT.txt")
    
    # Calculate statistics
    total_files = 0
    total_size = 0
    category_stats = {}
    
    for category, files in organized_files.items():
        if files:
            category_size = 0
            for filename in files:
                file_path = os.path.join(base_folder, category, filename)
                file_size = get_file_info(file_path)['size']
                category_size += file_size
            
            category_stats[category] = {
                'count': len(files),
                'size': category_size,
                'size_formatted': format_file_size(category_size)
            }
            total_files += len(files)
            total_size += category_size
    
    # Create detailed report content
    content = []
    content.append("📊 DETAILED ORGANIZATION REPORT")
    content.append("=" * 60)
    content.append(f"Generated on: {timestamp}")
    content.append(f"Base folder: {base_folder}")
    content.append("")
    
    content.append("📈 SUMMARY STATISTICS:")
    content.append(f"Total files: {total_files}")
    content.append(f"Total size: {format_file_size(total_size)}")
    content.append(f"Categories: {len([c for c in organized_files.values() if c])}")
    content.append("")
    
    content.append("📁 CATEGORY DETAILS:")
    content.append("-" * 40)
    
    for category, stats in category_stats.items():
        content.append(f"📁 {category}:")
        content.append(f"   Files: {stats['count']}")
        content.append(f"   Size: {stats['size_formatted']}")
        content.append("")
    
    content.append("=" * 60)
    content.append("End of detailed report")
    
    # Write detailed report
    report_content = "\n".join(content)
    return write_summary_file(report_path, report_content)

def validate_summary_creation(base_folder, organized_files):
    """Validate that summary creation is possible"""
    if not os.path.exists(base_folder):
        return False, "Base folder does not exist"
    
    if not os.path.isdir(base_folder):
        return False, "Base folder path is not a directory"
    
    try:
        # Test write access
        test_file = os.path.join(base_folder, "test_write.tmp")
        with open(test_file, 'w') as f:
            f.write("test")
        os.remove(test_file)
        return True, "Write access confirmed"
    except PermissionError:
        return False, "Permission denied - cannot write summaries"
    except Exception as e:
        return False, f"Error testing write access: {str(e)}" 