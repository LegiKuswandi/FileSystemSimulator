# commands.py
# Berisi definisi dari semua perintah yang didukung oleh sistem.

import os
import sys
from directory_operations import DirectoryOperations
from file_operations import FileOperations
from utils import UtilityCommands
from colorama import init, Fore, Style
import time

class CommandHandler:
    def __init__(self):
        self.root = None  # Direktori root dari sistem file
        self.current_directory = None  # Direktori saat ini yang aktif
        self.path = "/"  # Jalur direktori saat ini
        self.dir_ops = DirectoryOperations(self)  # Instance untuk operasi direktori
        self.file_ops = FileOperations(self)  # Instance untuk operasi file
        self.utils = UtilityCommands(self)  # Instance untuk utilitas perintah

    # Fungsi utama untuk menjalankan CLI
    def main(self):
        self.utils.cls_command()
        print(Fore.CYAN + Style.BRIGHT + """    
     _  __    _                             _      ______ 
    | |/ /   | |                           | |    |____  |
    | ' / ___| | ___  _ __ ___  _ __   ___ | | __     / / 
    |  < / _ \ |/ _ \| '_ ` _ \| '_ \ / _ \| |/ /    / /  
    | . \  __/ | (_) | | | | | | |_) | (_) |   <    / /   
    |_|\_\___|_|\___/|_| |_| |_| .__/ \___/|_|\_\  /_/    
                                | |                        
                                |_|                                                        
        """)
        print(Fore.CYAN + Style.BRIGHT +  "               ===========================")
        print(Fore.CYAN + Style.BRIGHT +  "                   Welcome to DAL OS  ")
        print(Fore.CYAN + Style.BRIGHT +  "               ===========================\n")
        print(Fore.WHITE + Style.BRIGHT + "   Thank you for trying to use this OS!")
        print(Fore.WHITE + Style.BRIGHT + "   Hope you enjoy!\n")
        print(Fore.WHITE + Style.BRIGHT + "   Type 'root' first, and u can enjoy using the command.\n")

        while True:  # Loop utama untuk CLI
            command = input(f"{self.path}$ ").strip().split()  # Membaca input pengguna dan membagi menjadi perintah dan argumen
            if not command:  # Jika tidak ada perintah yang diberikan, lanjutkan loop
                continue

            cmd = command[0].lower()  # Ambil perintah utama
            args = command[1:]  # Ambil argumen

            # Menjalankan perintah sesuai input pengguna
            if cmd == 'root':
                self.utils.root_command()
            elif self.root is None:  # Jika root belum diinisialisasi, minta pengguna untuk menginisialisasi root terlebih dahulu.
                print("Please initialize the root directory first by using the 'root' command.")
            elif cmd == 'help':
                self.utils.help_command()
            elif cmd == 'listdir':
                self.utils.listdir_command()
            elif cmd == 'mkdir' and len(args) == 1:
                self.dir_ops.mkdir_command(args[0])
            elif cmd == 'mkfile' and len(args) == 1:
                self.file_ops.mkfile_command(args[0])
            elif cmd == 'rmdir' and len(args) == 1:
                self.dir_ops.rmdir_command(args[0])
            elif cmd == 'rmfile' and len(args) == 1:
                self.file_ops.rmfile_command(args[0])
            elif cmd == 'cd' and len(args) == 1:
                self.dir_ops.cd_command(args[0])
            elif cmd == 'rename' and len(args) == 2:
                self.utils.rename_command(args[0], args[1])
            elif cmd == 'writefile' and len(args) == 1:
                self.file_ops.writefile_command(args[0])
            elif cmd == 'readfile' and len(args) == 1:
                self.file_ops.readfile_command(args[0])
            elif cmd == 'filesize' and len(args) == 1:
                self.file_ops.filesize_command(args[0])
            elif cmd == 'cls':
                self.utils.cls_command()
            elif cmd == 'shutdown':
                self.utils.shutdown_command()
            else:
                print("Unknown command. Type 'help' for a list of available commands.")
