from colorama import Fore
from Src.crypte import crypte
from Src.decrypte import decrypte

def parse_command(command: str):
    return command.strip().split()


def LoopShell():
    print(Fore.GREEN + "welcome to the Shell CRYPTAGE! Type 'help' for a list of commands." + Fore.RESET)
    while True:
        command = input(Fore.BLUE + ">>> " + Fore.RESET)
        command_parts = parse_command(command)
        if command_parts[0] == 'help':
            print(Fore.YELLOW + "Available commands:\n- help: Show this help message\n- exit: Exit the shell\n- crypte: Encrypt a message\n- decrypte: Decrypt a message" + Fore.RESET)
        elif command_parts[0] == 'exit':
            print(Fore.GREEN + "Exiting the shell. Goodbye!" + Fore.RESET)
            break
        elif command_parts[0] == 'crypte':
            print(Fore.CYAN + "Encrypting..." + Fore.RESET)
            if len(command_parts) != 3:
                print(Fore.RED + "Invalid number of arguments for 'crypte'. Usage: crypte <input_file> <output_file>" + Fore.RESET)
            else:
                crypte(command_parts[1], command_parts[2])
        elif command_parts[0] == 'decrypte':
            print(Fore.CYAN + "Decrypting..." + Fore.RESET)
            if len(command_parts) != 3:
                print(Fore.RED + "Invalid number of arguments for 'decrypte'. Usage: decrypte <input_file> <output_file>" + Fore.RESET)
            else:
                decrypte(command_parts[1], command_parts[2])
        else:
            print(Fore.RED + f"Unknown command: {command_parts[0]}. Type 'help' for a list of commands." + Fore.RESET)