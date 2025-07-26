# 📁 Folder Organizer

A modern, stylish GUI application built with Tkinter that automatically organizes files by type into categorized folders. **No OOP patterns used** - built with a clean functional approach.

## ✨ Features

- **Modern Dark Theme**: Beautiful flat UI design with a pleasant dark color palette
- **File Classification**: Automatically categorizes files into 10 different types:
  - 📸 Images (jpg, png, gif, etc.)
  - 🎥 Videos (mp4, avi, mov, etc.)
  - 📄 Documents (pdf, doc, txt, etc.)
  - 📊 Spreadsheets (xls, xlsx, csv, etc.)
  - 📋 Presentations (ppt, pptx, key, etc.)
  - 🎵 Audio (mp3, wav, flac, etc.)
  - 📦 Archives (zip, rar, 7z, etc.)
  - 💻 Code (py, js, html, etc.)
  - ⚙️ Executables (exe, msi, app, etc.)
  - 📁 Others (unrecognized file types)

- **Smart File Handling**: 
  - Handles duplicate filenames automatically
  - Preserves original file structure
  - Safe file operations with error handling

- **Summary Reports**: Generates detailed `summary.txt` files in each category folder listing:
  - Total number of files
  - File names with sizes
  - Timestamp of organization

- **Real-time Status**: Live progress updates and status logging
- **Threaded Operations**: Non-blocking UI during file operations

## 🏗️ Modular Architecture

The application is split into **5 separate modules** for better organization and understanding:

### 📱 `ui_manager.py` - User Interface
- Handles all GUI components and user interactions
- Manages dark theme styling and color scheme
- Provides real-time status updates and progress feedback
- Coordinates between different modules

### 📂 `file_organizer.py` - File Operations
- Handles file classification and movement
- Manages file categories and extensions
- Ensures safe file operations with duplicate handling
- Provides file validation and error handling

### 📝 `summary_writer.py` - Report Generation
- Generates detailed summary reports
- Creates formatted text files with file information
- Provides human-readable file size formatting
- Creates master and detailed reports

### 🔧 `file_utils.py` - Helper Functions
- Provides utility functions for file operations
- Includes file safety checks and information gathering
- Offers system information and time estimation
- Contains backup and validation functions

### 🚀 `main.py` - Application Entry Point
- Coordinates all modules
- Handles dependency checking
- Provides error handling and graceful exits
- Displays welcome messages and application info

## 🚀 How to Use

1. **Run the application**:
   ```bash
   python main.py
   ```

2. **Test with sample files**:
   ```bash
   python test_demo.py
   ```

3. **Follow the GUI**:
   - Click "📂 Select Folder"
   - Choose your folder
   - Click "🚀 Organize Files"
   - View results with "📊 View Summaries"

## 🎨 Design Features

- **Dark Theme**: Modern flat design with pleasant color palette
- **Responsive UI**: Clean layout with proper spacing and typography
- **Visual Feedback**: Progress bars, status updates, and color-coded buttons
- **Accessibility**: Clear labels, proper contrast, and intuitive navigation

## 🔧 Technical Details

### Requirements
- Python 3.6+
- Tkinter (included with Python)
- No external dependencies required

### File Categories Supported
The application recognizes and organizes files into these categories:

| Category | Extensions |
|----------|------------|
| Images | jpg, jpeg, png, gif, bmp, tiff, svg, webp |
| Videos | mp4, avi, mov, wmv, flv, mkv, webm, m4v |
| Documents | pdf, doc, docx, txt, rtf, odt, pages |
| Spreadsheets | xls, xlsx, csv, ods, numbers |
| Presentations | ppt, pptx, key, odp |
| Audio | mp3, wav, flac, aac, ogg, wma, m4a |
| Archives | zip, rar, 7z, tar, gz, bz2 |
| Code | py, js, html, css, java, cpp, c, php, rb, go |
| Executables | exe, msi, app, dmg, deb, rpm |
| Others | All unrecognized file types |

## 🛡️ Safety Features

- **Duplicate Handling**: Automatically renames files if duplicates exist
- **Error Recovery**: Graceful handling of file operation errors
- **File Safety**: Checks if files are accessible before moving
- **Thread Safety**: UI remains responsive during file operations
- **Validation**: Comprehensive input and file validation

## 📋 Example Output

After organizing a folder, you'll find:

```
Selected_Folder/
├── Images/
│   ├── photo1.jpg
│   ├── photo2.png
│   └── summary.txt
├── Documents/
│   ├── report.pdf
│   ├── notes.txt
│   └── summary.txt
├── Videos/
│   ├── video1.mp4
│   └── summary.txt
└── Others/
    ├── unknown_file.xyz
    └── summary.txt
```

Each `summary.txt` contains:
```
📁 Images - File Summary
==================================================
Generated on: 2024-01-15 14:30:25
Total files: 2
==================================================

  1. photo1.jpg                                    (2.5 MB)
  2. photo2.png                                    (1.8 MB)

==================================================
End of summary
```

## 🔮 Future Enhancements

The modular architecture makes it easy to add new features:

- **Custom Categories**: Allow users to define their own file categories
- **File Filters**: Add options to exclude certain file types
- **Batch Processing**: Process multiple folders at once
- **Undo Functionality**: Add ability to revert organization
- **File Preview**: Show thumbnails for images and videos
- **Export Options**: Generate reports in different formats

## 📁 File Structure

```
Folder organizer/
├── main.py              # Application entry point
├── ui_manager.py        # User interface management
├── file_organizer.py    # File classification and movement
├── summary_writer.py    # Report generation
├── file_utils.py        # Helper functions
├── test_demo.py         # Test script
└── README.md           # Documentation
```

## 🎯 Key Benefits of Modular Design

- **Easy to Understand**: Each module has a single, clear responsibility
- **Easy to Maintain**: Changes to one module don't affect others
- **Easy to Test**: Each module can be tested independently
- **Easy to Extend**: New features can be added as new modules
- **No OOP Complexity**: Simple functional approach without inheritance or polymorphism

## 📝 License

This project is open source and available under the MIT License.

---

**Happy Organizing! 🎉** 