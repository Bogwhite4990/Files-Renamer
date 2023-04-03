import os
import tkinter as tk
from tkinter import filedialog


def select_folder():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    return folder_path


def rename_files(folder_path, new_name):
    files = os.listdir(folder_path)
    print(f"Renaming {len(files)} files in folder {folder_path} to {new_name}")
    for i, file in enumerate(files):
        old_path = os.path.join(folder_path, file)
        new_path = os.path.join(folder_path, f"{new_name}_{i + 1}{os.path.splitext(file)[1]}")
        print(f"Renaming {old_path} to {new_path}")
        try:
            os.rename(old_path, new_path)
        except Exception as e:
            print(f"Error renaming {old_path}: {e}")


def main():
    folder_path = select_folder()
    new_name = input("Enter new file name: ")
    rename_files(folder_path, new_name)
    print("Files renamed successfully!")


if __name__ == '__main__':
    main()
