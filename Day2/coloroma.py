from colorama import Fore, Style

print(Fore.RED + 'Hello, World!' + Style.RESET_ALL)
print(Style.BRIGHT + 'This is bold text' + Style.RESET_ALL)
print(Fore.BLUE + '\x1b[4m' + 'Underlined and blue' + Style.RESET_ALL)