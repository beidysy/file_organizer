import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to organize files by their extensions
def organize_files(directory):
    # Supported file types and their respective folders
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
        'Documents': ['.pdf', '.docx', '.doc', '.txt', '.pptx', '.xlsx'],
        'Audio': ['.mp3', '.wav', '.aac', '.flac'],
        'Video': ['.mp4', '.avi', '.mkv', '.mov'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Scripts': ['.py', '.js', '.html', '.css'],
        'Others': []
    }

    # Create directories for each file type if they don't exist
    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files to respective directories
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in file_types.items():
                if file_name.lower().endswith(tuple(extensions)):
                    shutil.move(file_path, os.path.join(directory, folder, file_name))
                    moved = True
                    break
            if not moved:
                shutil.move(file_path, os.path.join(directory, 'Others', file_name))

    messagebox.showinfo("Success", "Files organized successfully!")

# Function to select a directory
def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        organize_files(directory)

# Create the main window
root = tk.Tk()
root.title("File Organizer")
root.geometry("300x150")

# Create and place the widgets
label = tk.Label(root, text="Select a directory to organize files:")
label.pack(pady=20)

button = tk.Button(root, text="Select Directory", command=select_directory)
button.pack(pady=20)

# Start the main event loop
root.mainloop()
