# Efesto_v1.0
from dataclasses \
    import dataclass
import colorama
from colorama import Fore, Style
import time

@dataclass()
class conexion:

    def comprobar_conexion():
        import socket

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)

        try:
            s.connect(("www.google.com", 80))
        except (socket.gaierror, socket.timeout):
            print(Fore.RED + "# Sin conexión a internet" + Style.RESET_ALL + Fore.MAGENTA + ' ¯\(°_°)/¯' + Style.RESET_ALL)
            return False
        else:
            print(Fore.GREEN + "# Con conexión a internet" + Style.RESET_ALL + Fore.LIGHTMAGENTA_EX + ' ¯\(O_O)/¯' + Style.RESET_ALL)
            return True
            s.close()

if (conexion.comprobar_conexion() == True):
    print(Fore.GREEN + '# Aqui inicia' + Style.RESET_ALL)
    time.sleep(1)
    import Preparacion
else:
    print(Fore.GREEN + '# Aqui no inicia por falta de internet...' + Style.RESET_ALL)










