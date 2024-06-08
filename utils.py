# utils.py
# Berisi fungsi utilitas seperti help_command, cls_command, dll.

import os
import sys

class UtilityCommands:
    def __init__(self, command_handler):
        self.command_handler = command_handler  # Instance dari CommandHandler

    # Menampilkan daftar perintah yang tersedia
    def help_command(self):
        print("Available commands:")
        print("  help      : Display this help message")
        print("  listdir   : List files and directories in the current directory")
        print("  mkdir     : Create a new directory")
        print("  mkfile    : Create a new file")
        print("  rmdir     : Remove a directory")
        print("  rmfile    : Remove a file")
        print("  cd        : Change directory")
        print("  root      : Initialize root directory")
        print("  cls       : Clear the screen")
        print("  rename    : Rename a file or directory")
        print("  writefile : Rename a file or directory")
        print("  readfile  : Rename a file or directory")
        print("  filesize  : Rename a file or directory")
        print("  shutdown  : Exit the CLI")

    # Menampilkan daftar file dan direktori dalam direktori saat ini
    def listdir_command(self):
        current_directory = self.command_handler.current_directory
        if not current_directory:  # Jika direktori saat ini kosong
            print("Directory is empty.")
        else:  # Jika tidak kosong, cetak struktur direktori
            self._print_directory_tree(current_directory, "")

    # Mencetak struktur direktori secara rekursif
    def _print_directory_tree(self, directory, prefix):
        for key in sorted(directory.keys()):  # Iterasi melalui setiap item dalam direktori secara berurutan
            if directory[key] is None:  # Jika item adalah file
                print(f"{prefix}├── {key}")
            else:  # Jika item adalah direktori
                print(f"{prefix}├── {key}/")
                self._print_directory_tree(directory[key], prefix + "│   ")

    # Inisialisasi direktori root
    def root_command(self):
        self.command_handler.root = {}  # Membuat direktori root baru
        self.command_handler.current_directory = self.command_handler.root  # Mengatur direktori saat ini ke root
        self.command_handler.path = "/"  # Mengatur jalur ke root
        print("Root directory initialized.")

    # Membersihkan layar
    def cls_command(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # Menjalankan perintah sistem untuk membersihkan layar

    # Mematikan sistem
    def shutdown_command(self):
        print("Shutting down...")
        sys.exit()  # Keluar dari program

    # Mengganti nama file atau direktori
    def rename_command(self, old_name, new_name):
        current_directory = self.command_handler.current_directory
        if old_name not in current_directory:  # Jika file atau direktori tidak ada
            print(f"'{old_name}' does not exist.")
        elif new_name in current_directory:  # Jika nama baru sudah ada
            print(f"'{new_name}' already exists.")
        else:  # Jika valid, ganti nama
            current_directory[new_name] = current_directory.pop(old_name)
            print(f"'{old_name}' renamed to '{new_name}'.")
