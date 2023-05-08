
from dataclasses \
    import dataclass
import subprocess
import time
import colorama
from colorama import Fore, Style

#Logo de programa


@dataclass
class instalacion_base:
    #Variable de tiempo de pausa
    tiempo_duracion = 5

    ##print(Fore.GREEN + '# Cargando distribucion de teclado de ' + Fore.RED + 'latinoamerica' + Style.RESET_ALL)
    ##subprocess.run(["loadkeys la-latin1"])

    print(Fore.GREEN + '# Cargando hora y fecha a systemctl' + Style.RESET_ALL)
    print(subprocess.Popen(["timedatectl", "set-ntp", "true"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)

    print(Fore.GREEN + '# Lista de particiones existentes' + Style.RESET_ALL)
    print(subprocess.Popen(["lsblk"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)

    print(Fore.GREEN + '# Informacion del disco' + Style.RESET_ALL)
    print(subprocess.Popen(["lsblk", "-l"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)
    time.sleep(10)

    print(Fore.GREEN + '# Limpiando tabla de particiones' + Style.RESET_ALL)
    print(subprocess.Popen(["sgdisk", "-Z", "/dev/sda"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)

    # crea la primera particion de 512MB
    print(Fore.GREEN + '# creando la primera particion de 512MB' + Style.RESET_ALL)
    print(subprocess.Popen(["sgdisk", "-n", "0:0:+512M", "-t", "0:ef00", "/dev/sda"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)

    # crea la segunda particion de 8GB
    print(Fore.GREEN + '# crea la segunda particion de 8GB' + Style.RESET_ALL)
    print(subprocess.Popen(["sgdisk", "-n", "0:0:+8G", "-t", "0:ef00", "/dev/sda"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)

    # crea la tercera particion con el espacio restante
    print(Fore.GREEN + '# crea la tercera particion con el espacio restante' + Style.RESET_ALL)
    print(subprocess.Popen(["sgdisk", "-n", "0:0:0", "-t", "0:ef00", "/dev/sda"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)

    #Limpiando pantalla
    subprocess.Popen(["clear"]).wait()

    #Esquema de particiones
    print(subprocess.Popen(["lsblk"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)

    #Pausar durante 5 segundos para comprobar particiones
    print(Fore.GREEN + '#Despues de 5 seg continuara en proceso...' + Style.RESET_ALL)
    time.sleep(5)

    # Formatear EFI
    print(Fore.RED + '# Formateando EFI' + Style.RESET_ALL)
    print(subprocess.Popen(["mkfs.fat", "-F32", "/dev/sda1"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)


    print(Fore.RED + '# Formateando swap' + Style.RESET_ALL)
    print(subprocess.Popen(["mkswap", "/dev/sda2"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)

    print(Fore.RED + '# Activando swap' + Style.RESET_ALL)
    print(subprocess.Popen(["swapon", "/dev/sda2"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)

    print(Fore.RED + '# Formateando raiz /' + Style.RESET_ALL)
    print(subprocess.Popen(["mkfs.btrfs", "/dev/sda3"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)

    print(Fore.GREEN + '# Montando raiz /' + Style.RESET_ALL)
    print(subprocess.Popen(["mount", "/dev/sda3", "/mnt"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)

    print(Fore.GREEN + '# Creando directorios de EFI' + Style.RESET_ALL)
    print(subprocess.Popen(["mkdir", "/mnt/boot", "&&", "mkdir", "/mnt/boot/efi"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)

    print(Fore.GREEN + '# Montando EFI' + Style.RESET_ALL)
    print(subprocess.Popen(["mount", "/dev/sda1", "/mnt/boot/efi"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)

    print(Fore.GREEN + '# Creando directorios de mirrorllist' + Style.RESET_ALL)
    print(subprocess.Popen(["mkdir", "/etc/pacman.d/mirrorlist"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)

    print(Fore.RED + '#Descargando base base-devel linux linux-zen nano zsh' + Style.RESET_ALL)
    print(subprocess.Popen(["pacstrap", "/mnt", "base", "base-devel", "linux", "linux-zen", "nano", "zsh"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)

    print(subprocess.Popen(["genfstab", "-U",  "/mnt", ">>", "/mnt/etc/fstab"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)

    print(subprocess.Popen(["mkdir", "/mnt/etc/fstab"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)
    subprocess.Popen(["clear"])

    print(Fore.GREEN + '## Accediendo al sistema vanilla recien instalado...' + Style.RESET_ALL)
    time.sleep(tiempo_duracion)
    print(subprocess.Popen(["arch-chroot", "/mnt"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)

    print(Fore.GREEN + '# Region pre-establecida /America/Mexico_City' + Style.RESET_ALL)
    print(subprocess.Popen(["ln", "-sf", "/usr/share/zoneinfo/America/Mexico_City /etc/localtime"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)

    print(Fore.GREEN + '# Poniendo el hardware ala hora' + Style.RESET_ALL)
    print(subprocess.Popen(["hwclock", "--systohc"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)

    print(Fore.GREEN + '# Estableciendo Idioma y distribucion de teclado' + Style.RESET_ALL)
    print(subprocess.Popen(["echo", "LANG=es_MX.UTF-8", ">", "/etc/locale.conf"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)
    print(subprocess.Popen(["echo", "KEYMAP=la-latin1", ">", "/etc/vconsole.conf"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)

    print(Fore.GREEN + '# Poniendo un nombre por defecto al equipo' + Style.RESET_ALL)
    print(subprocess.Popen(["echo", "PC", ">", "/etc/hostname"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)


    print(Fore.GREEN + '# Instalando y configurando el administrador red' + Style.RESET_ALL)
    print(subprocess.Popen(["pacman", "-S", "networkmanager", "--noconfirm"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)
    print(subprocess.Popen(["systemctl", "enable", "NetworkManager"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)

    print(Fore.GREEN + '# Instalando y configurando el bootloader' + Style.RESET_ALL)
    print(subprocess.Popen(["pacman", "-S", "grub", "efibootmgr", "--noconfirm"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)
    print(subprocess.Popen(["grub-install", "--target=x86_64-efi", "--efi-directory=/boot/efi"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)
    print(subprocess.Popen(["grub-mkconfig", "-o", "/boot/grub/grub.cfg"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)
    subprocess.run(["clear"])

@dataclass
class post_instalacion:
    tiempo_pausa = 5

    print(Fore.GREEN + '# Instalando entorno grafico y gestor de pantalla' + Style.RESET_ALL)
    time.sleep(tiempo_pausa)
    print(subprocess.Popen(["pacman", "-S", "gnome", "gdm", "--noconfirm"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)


    print(Fore.RED + '# configurando gestor de pantalla' + Style.RESET_ALL)
    print(subprocess.Popen(["systemctl", "enable", "gdm.service"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)

    subprocess.run(["clear"])

    print(Fore.GREEN + '# Instalando seleccion de software para compatibilidad...' + Style.RESET_ALL)
    print(subprocess.Popen(["pacman", "-S", "zsh", "neofetch", "wget", "curl", "yay", "zip", "tar", "tilix", "ntfs-3g",
                            "exfatprogs", "f2fs-tools", "udftools", "vlc", "--noconfirm"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)
    subprocess.run(["clear"])


@dataclass
class configuracion_personal:
    tiempo_pausa = 20

    print(Fore.RED + '# Cambiar la contraseña de root, despues verificar la contraseña \n'
                     '## Es sumamente importante de lo contrario no podra acceder al sistema \n'
                     '### Esto se realiza con el comando: passwd \n'
                     '#### Despues ingresar contraseña y verificar contraseña \n'
                     '##### El script se pausara 20 seg para que tome nota, ***realizar esto una vex terminado el programa*** \n' + Style.RESET_ALL)
    time.sleep(tiempo_pausa)

    print(Fore.GREEN + '# Añadiendo usuario *predeterminado*' + Style.RESET_ALL)
    print(subprocess.Popen(["useradd", "-m", "Predeterminado"]).wait(), Fore.GREEN, end='\n' + '# Ok \n' + Style.RESET_ALL)
    print(Fore.RED + '# Cambiar la contraseña de predeterminado, despues verificar la contraseña \n'
                     '## Es sumamente importante de lo contrario no podra acceder al sistema \n'
                     '### Esto de realisa con el comando: passwd predeterminado\n'
                     '#### Despues ingresar contraseña y verificar contraseña \n'
                     '##### El script se pausara 20 seg para que tome nota, ***realizar esto una vex terminado el programa*** \n' + Style.RESET_ALL)
    time.sleep(tiempo_pausa)
    print(Fore.WHITE+ '# Finalizado con exito' + Style.RESET_ALL)

