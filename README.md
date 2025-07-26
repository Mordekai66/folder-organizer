# Folder Organizer

**A modern, stylish desktop app** built with Tkinter that auto-organizes your files into categorized folders — all using a clean functional approach, **no OOP involved**. Simple, smart, and beautiful.

---

## Features

- **Modern Dark Theme** with flat UI design  
- **Automatic File Classification** into 10 categories:
  - 📸 Images
  - 🎥 Videos
  - 📄 Documents
  - 📊 Spreadsheets
  - 📋 Presentations
  - 🎵 Audio
  - 📦 Archives
  - 💻 Code
  - ⚙️ Executables
  - 📁 Others

- **Smart Handling**:
  - Resolves duplicate filenames
  - Preserves original folder structure
  - Handles errors gracefully

- **Summary Reports**:
  - Auto-generated `summary.txt` files with file details
  - Includes file names, sizes, and timestamps

- **Live Updates**:
  - Real-time status logging
  - Progress feedback with responsive UI

---

## Modular Architecture

The app is cleanly split into **5 logical modules**:

### `ui_manager.py` – GUI Layer  
- Builds the UI using Tkinter  
- Handles user interactions and theming  
- Updates status logs and progress in real-time  

### `file_organizer.py` – File Engine  
- Detects and classifies files  
- Manages file movement and renaming  
- Ensures safe operations with validations  

### `summary_writer.py` – Report Generator  
- Creates detailed and readable reports  
- Formats file sizes and timestamps  
- Handles per-folder and master reports  

### `file_utils.py` – Utility Toolkit  
- Gathers file info and performs checks  
- Provides helper tools for validation and backups  
- Includes system time estimation tools  

### `main.py` – App Entry Point  
- Orchestrates all modules  
- Manages startup, dependencies, and errors  
- Displays welcome messages and exits gracefully  

---

## How to Use

1. Run the app:
   ```bash
   python main.py
   ```

2. Try the test setup:
   ```bash
   python test_demo.py
   ```

3. Use the GUI:
   - Click **📂 Select Folder**
   - Choose a directory
   - Click **🚀 Organize Files**
   - Click **📊 View Summaries** to see results

---

## Technical Details

### Requirements
- Python 3.6+
- Tkinter (comes with Python)
- No external libraries needed

### Supported Categories

| Category      | Extensions                                     |
|---------------|------------------------------------------------|
| Images        | jpg, jpeg, png, gif, bmp, tiff, svg, webp      |
| Videos        | mp4, avi, mov, mkv, flv, webm, m4v             |
| Documents     | pdf, doc, docx, txt, rtf, odt, pages           |
| Spreadsheets  | xls, xlsx, csv, ods, numbers                   |
| Presentations | ppt, pptx, key, odp                            |
| Audio         | mp3, wav, flac, aac, ogg, wma, m4a             |
| Archives      | zip, rar, 7z, tar, gz, bz2                     |
| Code          | py, js, html, css, java, cpp, c, php, rb, go   |
| Executables   | exe, msi, app, dmg, deb, rpm                   |
| Others        | Unrecognized file types                        |

---

## Safety First

- **Duplicate Handling** – smart renaming to avoid overwrites  
- **Error Recovery** – handles access or move errors safely  
- **File Safety** – validates file accessibility before actions  
- **Validation** – every input and action is checked

---

## Example Output Structure

After organizing a folder, here's how it looks:

```
Your_Folder/
├── Images/
│   ├── photo1.jpg
│   └── summary.txt
├── Documents/
│   ├── notes.txt
│   └── summary.txt
├── Others/
│   ├── random_file.xyz
│   └── summary.txt
```

**Sample `summary.txt` content**:
```
Images - File Summary
==================================================
Generated on: 2024-01-15 14:30:25
Total files: 2
==================================================

  1. photo1.jpg                                    (2.5 MB)
  2. photo2.png                                    (1.8 MB)

==================================================
End of summary
```

---

## Planned Enhancements

- 🔧 Custom file categories  
- 🎯 File filters and exclusion rules  
- 🗃️ Batch folder processing  
- ↩️ Undo last organization
- 🧑‍💻 Support run in terminal/CMD

---

## Repository Structure

```
Folder Organizer/
├── main.py              # Entry point
├── ui_manager.py        # GUI logic
├── file_organizer.py    # File classification and sorting
├── summary_writer.py    # Report generation
├── file_utils.py        # Utility functions
├── test_demo.py         # Testing script
└── README.md            # This documentation
```

---

## License

This project is licensed under the **MIT License** – use it, remix it, and make it yours!  

---

> **Happy Organizing! Your messy folders won’t know what hit them!**
