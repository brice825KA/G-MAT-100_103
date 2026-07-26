from colorama import Fore
from Src.crypte import crypte
from Src.decrypte import decrypte


def LoopShell():
    print(Fore.GREEN + "welcome to the Shell CRYPTAGE! Type 'help' for a list of commands." + Fore.RESET)
    while True:
        command = input(Fore.BLUE + ">>> " + Fore.RESET)
        if command == 'help':
            print(Fore.YELLOW + "Available commands:\n- help: Show this help message\n- exit: Exit the shell\n- crypte: Encrypt a message\n- decrypte: Decrypt a message" + Fore.RESET)
        elif command == 'exit':
            print(Fore.GREEN + "Exiting the shell. Goodbye!" + Fore.RESET)
            break
        elif command == 'crypte':
            command_parts = command.split()
            if len(command_parts) != 1:
                print(Fore.RED + "Invalid number of arguments for 'crypte'. Usage: crypte <input_file> <output_file>" + Fore.RESET)
            else:
                message = input("Enter the message to encrypt: ")
                key = input("Enter the encryption key: ")
                print(Fore.CYAN + "Encrypting..." + Fore.RESET)
                crypte(message, key)
        elif command == 'decrypte':
            command_parts = command.split()
            if len(command_parts) != 1:
                print(Fore.RED + "Invalid number of arguments for 'decrypte'. Usage: decrypte <input_file> <output_file>" + Fore.RESET)
            else:
                message = input("Enter the message to decrypt: ")
                key = input("Enter the decryption key: ")
                print(Fore.CYAN + "Decrypting..." + Fore.RESET)
                decrypte(message, key)
        else:
            print(Fore.RED + f"Unknown command: {command_parts[0]}. Type 'help' for a list of commands." + Fore.RESET)