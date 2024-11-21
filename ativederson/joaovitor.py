import pyfiglet

text = "ola mundo"
ascii_art = pyfiglet.figlet_format(text)
print(ascii_art)

import pyfiglet

text = "Neymar"

ascii_art_standard = pyfiglet.figlet_format(text, font="standard")
print(ascii_art_standard)

ascii_art_slant = pyfiglet.figlet_format(text, font = "slant")
print(ascii_art_slant)

import pyfiglet
from colorama import Fore, Style

from colorama import init
init(autoreset=True)

text = "L"

ascii_art = pyfiglet.figlet_format(text, font = "standard")

print(Fore.CYAN + Style.BRIGHT + ascii_art)

import pyfiglet
from colorama import Fore, Style, init

init()
print(Fore.RED + "")
print(Fore.BLUE + "")
print(Fore.WHITE + "")
print(Fore.YELLOW + "")
print(Fore.GREEN+ "")
