"""
UI Manager - Handles all user interface components
No OOP patterns used - functional approach
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from datetime import datetime
import threading
import os

# Global variables for UI state
root_window = None
selected_folder = ""
progress_var = None
status_text = None
organize_btn = None
select_btn = None
summary_btn = None
progress_bar = None

# Color scheme for dark theme
COLORS = {
    'bg_dark': '#1e1e1e',
    'bg_medium': '#2d2d2d',
    'bg_light': '#3d3d3d',
    'accent': '#007acc',
    'accent_hover': '#005a9e',
    'text': '#ffffff',
    'text_secondary': '#cccccc',
    'success': '#4caf50',
    'warning': '#ff9800',
    'error': '#f44336'
}

def create_main_window():
    """Create and configure the main application window"""
    global root_window
    root_window = tk.Tk()
    root_window.title("Folder Organizer")
    root_window.geometry("600x500")
    root_window.resizable(False, False)
    root_window.configure(bg=COLORS['bg_dark'])
    return root_window

def setup_main_container():
    """Create the main container frame"""
    main_frame = tk.Frame(root_window, bg=COLORS['bg_dark'])
    main_frame.pack(fill='both', expand=True, padx=20, pady=20)
    return main_frame

def create_title_section(main_frame):
    """Create the title and description section"""
    # Title
    title_label = tk.Label(
        main_frame,
        text="📁 Folder Organizer",
        font=('Segoe UI', 24, 'bold'),
        fg=COLORS['accent'],
        bg=COLORS['bg_dark']
    )
    title_label.pack(pady=(0, 30))
    
    # Description
    desc_label = tk.Label(
        main_frame,
        text="Automatically organize your files by type into categorized folders",
        font=('Segoe UI', 10),
        fg=COLORS['text_secondary'],
        bg=COLORS['bg_dark'],
        wraplength=500
    )
    desc_label.pack(pady=(0, 30))

def create_folder_section(main_frame):
    """Create the folder selection section"""
    folder_frame = tk.Frame(main_frame, bg=COLORS['bg_dark'])
    folder_frame.pack(fill='x', pady=(0, 20))
    
    folder_label = tk.Label(
        folder_frame,
        text="Selected Folder:",
        font=('Segoe UI', 12, 'bold'),
        fg=COLORS['text'],
        bg=COLORS['bg_dark']
    )
    folder_label.pack(anchor='w', pady=(0, 10))
    
    # Folder path display
    global progress_var
    progress_var = tk.StringVar(value="No folder selected")
    folder_display = tk.Label(
        folder_frame,
        textvariable=progress_var,
        font=('Segoe UI', 9),
        fg=COLORS['text_secondary'],
        bg=COLORS['bg_medium'],
        anchor='w',
        padx=10,
        pady=8,
        relief='flat',
        wraplength=500
    )
    folder_display.pack(fill='x', pady=(0, 10))

def create_buttons_section(main_frame):
    """Create the buttons section"""
    buttons_frame = tk.Frame(main_frame, bg=COLORS['bg_dark'])
    buttons_frame.pack(fill='x', pady=(0, 20))
    
    global select_btn, organize_btn, summary_btn
    
    # Select folder button
    select_btn = tk.Button(
        buttons_frame,
        text="📂 Select Folder",
        font=('Segoe UI', 11, 'bold'),
        fg=COLORS['text'],
        bg=COLORS['accent'],
        activebackground=COLORS['accent_hover'],
        activeforeground=COLORS['text'],
        relief='flat',
        padx=20,
        pady=10,
        cursor='hand2',
        command=handle_folder_selection
    )
    select_btn.pack(side='left', padx=(0, 10))
    
    # Organize button
    organize_btn = tk.Button(
        buttons_frame,
        text="🚀 Organize Files",
        font=('Segoe UI', 11, 'bold'),
        fg=COLORS['text'],
        bg=COLORS['success'],
        activebackground='#45a049',
        activeforeground=COLORS['text'],
        relief='flat',
        padx=20,
        pady=10,
        cursor='hand2',
        command=handle_organize_files,
        state='disabled'
    )
    organize_btn.pack(side='left', padx=(0, 10))
    
    # View summaries button
    summary_btn = tk.Button(
        buttons_frame,
        text="📊 View Summaries",
        font=('Segoe UI', 11, 'bold'),
        fg=COLORS['text'],
        bg=COLORS['warning'],
        activebackground='#e68900',
        activeforeground=COLORS['text'],
        relief='flat',
        padx=20,
        pady=10,
        cursor='hand2',
        command=handle_view_summaries,
        state='disabled'
    )
    summary_btn.pack(side='left')

def create_progress_section(main_frame):
    """Create the progress section"""
    progress_frame = tk.Frame(main_frame, bg=COLORS['bg_dark'])
    progress_frame.pack(fill='x', pady=(20, 0))
    
    global progress_var
    progress_label = tk.Label(
        progress_frame,
        textvariable=progress_var,
        font=('Segoe UI', 10),
        fg=COLORS['text_secondary'],
        bg=COLORS['bg_dark']
    )
    progress_label.pack(anchor='w', pady=(0, 10))
    
    # Progress bar
    global progress_bar
    progress_bar = ttk.Progressbar(
        progress_frame,
        mode='indeterminate',
        length=560
    )
    progress_bar.pack(fill='x')

def create_status_section(main_frame):
    """Create the status section"""
    status_frame = tk.Frame(main_frame, bg=COLORS['bg_dark'])
    status_frame.pack(fill='both', expand=True, pady=(20, 0))
    
    status_label = tk.Label(
        status_frame,
        text="Status:",
        font=('Segoe UI', 12, 'bold'),
        fg=COLORS['text'],
        bg=COLORS['bg_dark']
    )
    status_label.pack(anchor='w', pady=(0, 10))
    
    # Status text area
    global status_text
    status_text = tk.Text(
        status_frame,
        height=8,
        font=('Consolas', 9),
        fg=COLORS['text'],
        bg=COLORS['bg_medium'],
        insertbackground=COLORS['text'],
        relief='flat',
        padx=10,
        pady=10,
        wrap='word'
    )
    status_text.pack(fill='both', expand=True)
    
    # Scrollbar for status text
    status_scrollbar = tk.Scrollbar(status_frame, orient='vertical', command=status_text.yview)
    status_scrollbar.pack(side='right', fill='y')
    status_text.configure(yscrollcommand=status_scrollbar.set)

def apply_dark_theme():
    """Apply dark theme styling to ttk widgets"""
    style = ttk.Style()
    style.theme_use('clam')
    
    # Configure ttk styles
    style.configure('TProgressbar',
                   background=COLORS['accent'],
                   troughcolor=COLORS['bg_medium'],
                   borderwidth=0,
                   lightcolor=COLORS['accent'],
                   darkcolor=COLORS['accent'])

def handle_folder_selection():
    """Handle folder selection button click"""
    global selected_folder
    folder = filedialog.askdirectory(title="Select folder to organize")
    if folder:
        selected_folder = folder
        progress_var.set(f"📁 {folder}")
        organize_btn.config(state='normal')
        log_status(f"✅ Selected folder: {folder}")
    else:
        log_status("❌ No folder selected")

def handle_organize_files():
    """Handle organize files button click"""
    if not selected_folder:
        messagebox.showerror("Error", "Please select a folder first!")
        return
    
    # Disable buttons during operation
    organize_btn.config(state='disabled')
    select_btn.config(state='disabled')
    progress_bar.start()
    progress_var.set("Organizing files...")
    
    # Run in separate thread to prevent UI freezing
    thread = threading.Thread(target=organize_files_thread)
    thread.daemon = True
    thread.start()

def organize_files_thread():
    """Thread function for file organization"""
    try:
        # Import here to avoid circular imports
        from file_organizer import organize_folder
        from summary_writer import generate_summaries
        
        # Organize files
        organized_files = organize_folder(selected_folder)
        
        # Generate summaries
        generate_summaries(selected_folder, organized_files)
        
        # Update UI in main thread
        root_window.after(0, organize_complete, organized_files)
        
    except Exception as e:
        root_window.after(0, organize_error, str(e))

def organize_complete(organized_files):
    """Handle completion of file organization"""
    progress_bar.stop()
    progress_var.set("✅ Organization complete!")
    
    # Re-enable buttons
    organize_btn.config(state='normal')
    select_btn.config(state='normal')
    summary_btn.config(state='normal')
    
    # Log results
    total_files = sum(len(files) for files in organized_files.values())
    log_status(f"✅ Successfully organized {total_files} files")
    
    for category, files in organized_files.items():
        if files:
            log_status(f"📁 {category}: {len(files)} files")
    
    messagebox.showinfo("Success", f"Successfully organized {total_files} files!")

def organize_error(error_msg):
    """Handle errors during organization"""
    progress_bar.stop()
    progress_var.set("❌ Organization failed")
    
    # Re-enable buttons
    organize_btn.config(state='normal')
    select_btn.config(state='normal')
    
    log_status(f"❌ Error: {error_msg}")
    messagebox.showerror("Error", f"Failed to organize files:\n{error_msg}")

def handle_view_summaries():
    """Handle view summaries button click"""
    if selected_folder and os.path.exists(selected_folder):
        os.startfile(selected_folder)
        log_status("📂 Opened organized folder")
    else:
        messagebox.showwarning("Warning", "No organized folder available")

def log_status(message):
    """Add a message to the status log"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    status_text.insert('end', f"[{timestamp}] {message}\n")
    status_text.see('end')

def get_selected_folder():
    """Get the currently selected folder"""
    return selected_folder

def setup_ui():
    """Setup the complete user interface"""
    create_main_window()
    apply_dark_theme()
    
    main_frame = setup_main_container()
    create_title_section(main_frame)
    create_folder_section(main_frame)
    create_buttons_section(main_frame)
    create_progress_section(main_frame)
    create_status_section(main_frame)

def run_application():
    """Start the application"""
    root_window.mainloop() 