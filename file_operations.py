# file_operations.py
# Berisi operasi yang berkaitan dengan file (mkfile, rmfile, dll).

import sys

class FileOperations:
    def __init__(self, command_handler):
        self.command_handler = command_handler  # Instance dari CommandHandler

    # Membuat file baru
    def mkfile_command(self, file_name):
        current_directory = self.command_handler.current_directory
        if file_name in current_directory:  # Jika file sudah ada
            print(f"File '{file_name}' already exists.")
        else:  # Jika belum ada, buat file baru
            current_directory[file_name] = None
            print(f"File '{file_name}' created.")

    # Menghapus file
    def rmfile_command(self, file_name):
        current_directory = self.command_handler.current_directory
        if file_name not in current_directory:  # Jika file tidak ada
            print(f"File '{file_name}' does not exist.")
        elif current_directory[file_name] is None or not None:  # Jika file ada
            del current_directory[file_name]
            print(f"File '{file_name}' removed.")
        else:  # Jika bukan file
            print(f"'{file_name}' is not a file.")

    # Menulis file
    def writefile_command(self, file_name):
        current_directory = self.command_handler.current_directory
        if file_name not in current_directory:  # Jika file tidak ada
            print(f"File '{file_name}' does not exist.")
        elif current_directory[file_name] is None or not None:  # Jika file ada
            print(f"============================================================================================")
            print(f" Writing file {file_name}")
            print(f"============================================================================================")
            print(f"")
            print(f" Press Ctrl-Z and Enter to save the file.\n")
            content = sys.stdin.read()
            current_directory[file_name] = content
            print(f"File '{file_name}' succesfully edited.")
        else:  # Jika bukan file
            print(f"'{file_name}' is not a file.")

    # Membaca file
    def readfile_command(self, file_name):
        current_directory = self.command_handler.current_directory
        if file_name not in current_directory:  # Jika file tidak ada
            print(f"File '{file_name}' does not exist.")
        elif current_directory[file_name] is None:  # Jika file ada
            print(f"============================================================================================")
            print(f"Opening file '{file_name}' ...")
            print(f"============================================================================================")
            print(f"The content is empty")
            print(f"============================================================================================")
            input("\n For exit, press enter.")
            print(f"============================================================================================")
        elif current_directory[file_name] is not None:
            print(f"============================================================================================")
            print(f"Opening file '{file_name}' ...")
            print(f"============================================================================================")
            print(f"{current_directory[file_name]}")
            print(f"============================================================================================")
            input("\n For exit, press enter.")
            print(f"============================================================================================")
        else:  # Jika bukan file
            print(f"'{file_name}' is not a file.")

    # Menulis file
    def filesize_command(self, file_name):
        current_directory = self.command_handler.current_directory
        if file_name not in current_directory:  # Jika file tidak ada
            print(f"File '{file_name}' does not exist.")
        elif current_directory[file_name] is None or not None:  # Jika file ada
            size = len(current_directory[file_name])
            print(f"Size of file {file_name} {size} bytes")