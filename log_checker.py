import os
import tkinter as tk
from tkinter import filedialog
import chardet
import csv
import glob
import datetime


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
                if 'ERROR ' in line:
                    error_lines.append(line.strip())
                elif 'error ' in line:
                    pass
                elif '_ERROR' in line:
                    pass

        print(f"{i} of {num_files} files processed")
        i += 1

    # count unique errors and their occurrences
    unique_errors = {}
    for line in error_lines:
        line_cleaned = line.split('(')[0].strip()
        if line_cleaned not in unique_errors:
            unique_errors[line_cleaned] = 1
        else:
            unique_errors[line_cleaned] += 1

    if unique_errors:
        with open('error_log.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(['Error', 'Occurrences'])

            for error, count in unique_errors.items():
                writer.writerow([f"{error} ({count} occurrences)"])

        print(f"{len(unique_errors)} unique errors found. See error_log.csv for details.")
    else:
        print("No errors found.")



root = tk.Tk()
root.withdraw()
folder_path = filedialog.askdirectory(title="Select folder to check logs")
if folder_path:
    check_logs(folder_path)
