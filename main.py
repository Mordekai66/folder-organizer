"""
Main Application - Folder Organizer
Entry point that coordinates all modules
No OOP patterns used - functional approach
"""

import sys
import os

def check_dependencies():
    """Check if all required modules are available"""
    required_modules = [
        'ui_manager',
        'file_organizer', 
        'summary_writer',
        'file_utils'
    ]
    
    missing_modules = []
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            missing_modules.append(module)
    
    if missing_modules:
        print("❌ Error: Missing required modules:")
        for module in missing_modules:
            print(f"   - {module}.py")
        print("\nPlease ensure all files are in the same directory.")
        return False
    
    return True

def display_welcome_message():
    """Display welcome message and application info"""
    print("=" * 60)
    print("📁 Folder Organizer - Modern File Management Tool")
    print("=" * 60)
    print("✨ Features:")
    print("   • Automatic file categorization by type")
    print("   • Modern dark theme GUI")
    print("   • Detailed summary reports")
    print("   • Safe file operations with error handling")
    print("   • Real-time progress updates")
    print("=" * 60)
    print("🚀 Starting application...")
    print()

def main():
    """Main application entry point"""
    try:
        # Check dependencies
        if not check_dependencies():
            sys.exit(1)
        
        # Display welcome message
        display_welcome_message()
        
        # Import modules
        from ui_manager import setup_ui, run_application
        
        # Setup and run the application
        setup_ui()
        run_application()
        
    except KeyboardInterrupt:
        print("\n👋 Application interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("Please check the error details above.")
        sys.exit(1)

if __name__ == "__main__":
    main() 