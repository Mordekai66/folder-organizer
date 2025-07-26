
"""
Test Demo Script for Folder Organizer
Creates sample files in different categories to test the application
"""

import os
import shutil
from pathlib import Path

def create_test_files():
    """Create sample files for testing the folder organizer"""
    
    # Create test directory
    test_dir = Path("test_folder")
    test_dir.mkdir(exist_ok=True)
    
    # Sample files to create
    test_files = {
        "sample_image.jpg": "Images",
        "vacation_photo.png": "Images", 
        "screenshot.gif": "Images",
        "document.pdf": "Documents",
        "notes.txt": "Documents",
        "report.docx": "Documents",
        "presentation.pptx": "Presentations",
        "meeting_slides.ppt": "Presentations",
        "data.xlsx": "Spreadsheets",
        "budget.csv": "Spreadsheets",
        "video.mp4": "Videos",
        "tutorial.avi": "Videos",
        "music.mp3": "Audio",
        "podcast.wav": "Audio",
        "archive.zip": "Archives",
        "backup.rar": "Archives",
        "script.py": "Code",
        "website.html": "Code",
        "styles.css": "Code",
        "program.exe": "Executables",
        "installer.msi": "Executables",
        "unknown_file.xyz": "Others"
    }
    
    print("Creating test files...")
    
    for filename, category in test_files.items():
        file_path = test_dir / filename
        
        # Create empty files (you can add content if needed)
        with open(file_path, 'w') as f:
            f.write(f"This is a sample {category} file: {filename}\n")
            f.write("Created for testing the Folder Organizer application.\n")
        
        print(f"✅ Created: {filename} ({category})")
    
    print(f"\n🎉 Test folder created at: {test_dir.absolute()}")
    print("You can now run the Folder Organizer application and select this folder!")
    
    return str(test_dir.absolute())

def cleanup_test_files():
    """Remove test files"""
    test_dir = Path("test_folder")
    if test_dir.exists():
        shutil.rmtree(test_dir)
        print("🧹 Cleaned up test folder")

if __name__ == "__main__":
    print("=" * 50)
    print("📁 Folder Organizer - Test Demo")
    print("=" * 50)
    
    # Check if test folder already exists
    if Path("test_folder").exists():
        print("⚠️  Test folder already exists!")
        response = input("Do you want to recreate it? (y/n): ")
        if response.lower() == 'y':
            cleanup_test_files()
            test_path = create_test_files()
        else:
            print("Using existing test folder.")
            test_path = str(Path("test_folder").absolute())
    else:
        test_path = create_test_files()
    
    print("\n" + "=" * 50)
    print("📋 Next Steps:")
    print("1. Run: python file_organizer_app.py")
    print("2. Click '📂 Select Folder'")
    print(f"3. Choose: {test_path}")
    print("4. Click '🚀 Organize Files'")
    print("5. Watch the magic happen! ✨")
    print("=" * 50) 