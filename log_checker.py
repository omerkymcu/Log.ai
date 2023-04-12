import os
import tkinter as tk
from tkinter import filedialog, ttk
import chardet
import csv
import glob


def get_encoding_type(file):
    with open(file, 'rb') as f:
        rawdata = f.read()
    return chardet.detect(rawdata)['encoding']


def check_logs(folder_path):
    logs = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.log') or file.endswith('.txt'):
                logs.append(os.path.join(root, file))
    num_files = len(logs)
    i = 1
    error_lines = []
    for file in logs:
        enc = get_encoding_type(file)
        with open(file, mode='r', encoding=enc, errors='ignore') as f:
            for j, line in enumerate(f):
                if 'error' in line.lower():
                    error_lines.append([file, j + 1, line.strip()])

        print(f"{i} of {num_files} files processed")
        i += 1

    if error_lines:
        with open('error_log.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(['File Path', 'Line Number', 'Error'])

            for line in error_lines:
                writer.writerow(line)

        root = tk.Tk()
        root.title("Error Lines")
        root.geometry("1024x768")

        textbox = tk.Text(root)
        textbox.pack(fill="both", expand=True)

        # Add a Copy button to copy the error lines to the clipboard
        copy_button = ttk.Button(root, text="Copy", command=lambda: root.clipboard_append(textbox.get("1.0", "end-1c")))
        copy_button.pack(side="bottom", padx=10, pady=10)

        # Add a scrollbar to the text box
        scrollbar = ttk.Scrollbar(root, orient="vertical", command=textbox.yview)
        scrollbar.pack(side="right", fill="y")

        textbox.config(yscrollcommand=scrollbar.set)

        # Split error lines into columns based on whitespace
        for line in error_lines:
            parts = line
            filepath = parts[0]
            line_number = parts[1]
            error = parts[2]
            textbox.insert("end", f"{filepath:<60}{line_number:<10}{error}\n")

        root.mainloop()
    else:
        print("No errors found.")


folder_path = filedialog.askdirectory()
if folder_path:
    check_logs(folder_path)
