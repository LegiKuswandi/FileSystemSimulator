# file_operations.py
# Berisi operasi yang berkaitan dengan file (mkfile, rmfile, dll).

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
        elif current_directory[file_name] is None:  # Jika file ada
            del current_directory[file_name]
            print(f"File '{file_name}' removed.")
        else:  # Jika bukan file
            print(f"'{file_name}' is not a file.")
