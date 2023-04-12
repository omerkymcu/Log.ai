import os
import tkinter as tk
from tkinter import filedialog
import chardet
import glob

def get_encoding_type(file):
    with open(file, 'rb') as f:
        rawdata = f.read()
    return chardet.detect(rawdata)['encoding']

def check_logs(folder_path):
    logs = []
    for file in glob.glob(os.path.join(folder_path, '*.log')):
        logs.append(file)
    for file in glob.glob(os.path.join(folder_path, '*.txt')):
        logs.append(file)
    num_files = len(logs)
    i = 1
    error_lines = []
    for file in logs:
        enc = get_encoding_type(file)
        with open(file, mode='r', encoding=enc, errors='ignore') as f:
            for j, line in enumerate(f):
                if 'error' in line.lower():
                    error_lines.append(f"{file}, Line {j + 1}: {line.strip()}")
        print(f"{i} of {num_files} files processed")
        i += 1

    if error_lines:
        root = tk.Tk()
        root.title("Error Lines")
        root.geometry("800x600")

        # Create a frame to hold the columns
        frame = tk.Frame(root)
        frame.pack(fill="both", expand=True)

        # Calculate the width of the columns based on the width of the window
        column_width = (root.winfo_width() // 3) - 10

        # Create labels for each column
        file_label = tk.Label(frame, text="File", width=column_width)
        line_label = tk.Label(frame, text="Line", width=column_width)
        error_label = tk.Label(frame, text="Error", width=column_width)

        # Pack the labels into the frame
        file_label.pack(side="left")
        line_label.pack(side="left")
        error_label.pack(side="left")

        # Add a separator line
        separator = tk.Frame(frame, height=2, bd=1, relief="sunken")
        separator.pack(fill="x")

        for line in error_lines:
            # Split the line into file, line number, and error message
            parts = line.split(": ")
            file = parts[0]
            line_number = parts[1]
            error = parts[2].strip()

            # Create labels for each part
            file_label = tk.Label(frame, text=file, width=column_width, anchor="w")
            line_label = tk.Label(frame, text=line_number, width=column_width, anchor="w")
            error_label = tk.Label(frame, text=error, width=column_width, anchor="w")

            # Pack the labels into the frame
            file_label.pack(side="left", fill="x")
            line_label.pack(side="left", fill="x")
            error_label.pack(side="left", fill="x")

        root.mainloop()
    else:
        print("No errors found.")


folder_path = filedialog.askdirectory()
check_logs(folder_path)
