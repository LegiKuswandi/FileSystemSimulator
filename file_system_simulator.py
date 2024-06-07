# file_system_simulator.py
# File utama yang menginisialisasi program dan menjalankan CLI.

from commands import CommandHandler

# Memulai eksekusi program
if __name__ == "__main__":
    command_handler = CommandHandler()  # Membuat instance CommandHandler
    command_handler.main()  # Memulai loop utama untuk CLI
