from dataclasses \
    import dataclass
import subprocess
import time
import colorama
from colorama import Fore, Style

@dataclass()
class preparacion:

    print(Fore.GREEN + '# Preparacion para iniciar el script' + Style.RESET_ALL)
    print(subprocess.Popen(["loadkeys", "la-latin1"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)
    print(subprocess.Popen(["pacman", "-Sy"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)
    print(subprocess.Popen(["pacman", "-S", "python", "--noconfirm"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)
    print(subprocess.Popen(["pacman", "-S", "python-pip", "--noconfirm"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)
    print(subprocess.Popen(["python", "-m", "pip", "install", "colorama"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)
    print(Fore.GREEN + '# Limpiando..\n' + Style.RESET_ALL, subprocess.Popen(["clear"]).wait(), Fore.GREEN, end='\n' + '# Ok \n')

    print('# El script continuara en 5seg', end='\n'+ '# Ok' + Style.RESET_ALL)

    for contador in range(0, 5):
        if range != 5:
            print(Fore.BLUE, (contador - 5) * (-1), Style.RESET_ALL, end=" ")
        time.sleep(1)

    print(end='\n' + Fore.GREEN + '# Iniciando Efesto' + Style.RESET_ALL)

@dataclass
class hola:
    for ok in range(0, 6):
        match ok:
            case 0:
                print(Fore.LIGHTRED_EX + '     __  __           _           _        ___  ')
            case 1:
                print('    /__\/ _| ___  ___| |_ ___    / |      / _ \ ')
            case 2:
                print('   /_\ | |_ / _ \/ __| __/ _ \   | |     | | | |')
            case 3:
                print('  //__ |  _|  __/\__ \ || (_) |  | |  _  | |_| |')
            case 4:
                print('  \__/ |_|  \___||___/\__\___/   |_| (_)  \___/ ')
            case 5:
                print('\n' + Fore.GREEN + '# OK' + Style.RESET_ALL)
            case _:
                exit(True)
        time.sleep(0.25)


