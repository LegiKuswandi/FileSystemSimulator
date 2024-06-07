# directory_operations.py
# Berisi operasi yang berkaitan dengan direktori (mkdir, rmdir, cd, dll).

class DirectoryOperations:
    def __init__(self, command_handler):
        self.command_handler = command_handler  # Instance dari CommandHandler

    # Membuat direktori baru
    def mkdir_command(self, directory_name):
        current_directory = self.command_handler.current_directory
        if directory_name in current_directory:  # Jika direktori sudah ada
            print(f"Directory '{directory_name}' already exists.")
        else:  # Jika belum ada, buat direktori baru
            current_directory[directory_name] = {}
            print(f"Directory '{directory_name}' created.")

    # Menghapus direktori
    def rmdir_command(self, directory_name):
        current_directory = self.command_handler.current_directory
        if directory_name not in current_directory:  # Jika direktori tidak ada
            print(f"Directory '{directory_name}' does not exist.")
        elif isinstance(current_directory[directory_name], dict):  # Jika direktori ada dan kosong
            if current_directory[directory_name]:  # Jika direktori tidak kosong
                print(f"Directory '{directory_name}' is not empty.")
            else:  # Jika kosong, hapus direktori
                del current_directory[directory_name]
                print(f"Directory '{directory_name}' removed.")
        else:  # Jika bukan direktori
            print(f"'{directory_name}' is not a directory.")

    # Mengganti direktori saat ini
    def cd_command(self, directory_name):
        command_handler = self.command_handler
        if directory_name == "/":  # Jika ingin pindah ke root
            command_handler.current_directory = command_handler.root
            command_handler.path = "/"
        elif directory_name == "..":  # Jika ingin pindah ke direktori induk
            if command_handler.path != "/":
                command_handler.path = "/".join(command_handler.path.rstrip("/").split("/")[:-1])
                if command_handler.path == "":
                    command_handler.path = "/"
                command_handler.current_directory = self._get_directory_from_path(command_handler.path)
        elif directory_name in command_handler.current_directory and isinstance(command_handler.current_directory[directory_name], dict):
            # Jika direktori ada dan valid, pindah ke direktori tersebut
            command_handler.current_directory = command_handler.current_directory[directory_name]
            if command_handler.path == "/":
                command_handler.path = f"/{directory_name}"
            else:
                command_handler.path = f"{command_handler.path}/{directory_name}"
        else:  # Jika direktori tidak ada
            print(f"Directory '{directory_name}' does not exist.")

    # Mendapatkan direktori dari jalur yang diberikan
    def _get_directory_from_path(self, path):
        parts = path.strip("/").split("/")  # Membagi jalur menjadi bagian-bagian
        directory = self.command_handler.root
        for part in parts:  # Iterasi melalui setiap bagian untuk mendapatkan direktori yang sesuai
            if part:
                directory = directory[part]
        return directory
