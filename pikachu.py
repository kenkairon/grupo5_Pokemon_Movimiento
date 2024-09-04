"""
sys: Proporciona acceso a algunas variables utilizadas o mantenidas por el intérprete,
 y a funciones que interactúan con el intérprete.
time: Proporciona varias funciones relacionadas con el tiempo,
 en este caso se usa sleep para pausar la ejecución.
"""
import sys
import time

def clear_console():
    # Mover el cursor al inicio de la pantalla
    sys.stdout.write('\033[H')
    
    # Borrar todas las líneas desde el cursor hasta el final de la pantalla
    sys.stdout.write('\033[J')
    
    # Asegurar que los cambios se reflejen inmediatamente
    sys.stdout.flush()

"""
t: Tiempo en segundos que se espera entre cada actualización de la pantalla.
T: Un valor que define el número total de ciclos en el bucle for.
u: Calcula la longitud de una cadena de espacios basada en T.
e, n, l: Variables no utilizadas en el código proporcionado.
cont: Contador para el número de ciclos en el bucle while.
"""

t = 0.2
T = 5  # Debe ser divisible por 2
u = T/2 - 1
e = " "
n = " "
l = " " * int(u)
cont = 0


"""
El bucle while ejecuta el código dentro hasta que cont sea menor que 10.
Dentro de este bucle, un bucle for itera de 1 a T-1 (es decir, 5-1 en este caso).
Dependiendo del valor de i, se imprime un conjunto diferente de líneas de arte ASCII.
Después de imprimir las líneas, el código espera t segundos (time.sleep(t)) y luego limpia la pantalla (clear_console()).
"""
while cont < 10:
    for i in range(1, T):
        clear_console()
        if i == 1:
            # Muestra una imagen en ASCII art
            print(f"⣿⣿⣿⠟⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ")
        print(f"⣿⣿⣿⠠⣿⣿⣷⣶⣭⣝⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ")
        print(f"⣿⣿⣿⡌⢿⣿⣿⣿⣿⣿⣿⣿⢆⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ")
        print(f"⣿⣿⣿⣧⣤⣶⣌⣉⣩⢻⣿⡏⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ")
        print(f"⣿⣿⣿⣿⣿⣿⣿⣿⡟⣸⣿⣤⣍⡛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ")
        print(f"⣿⣿⣿⣿⣿⣿⣿⣿⣷⣬⣉⣩⠹⢃⣽⣿⣿⣿⣿⣿⣿⠿⠻⠇⠀⢉⣙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ")
        print(f"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣌⡀⠀⢹⢿⡿⢋⡁⠀⢠⣀⠀⢰⣦⣉⠛⠧⠉⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ")
        print(f"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⢀⣴⣿⣧⠄⢸⣿⠂⢠⣍⡛⠿⣶⣶⣶⣾⣶⣬⣙⢿⣿⣿⣿⣿ ")
        print(f"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣼⣿⣿⣿⣿⣿⣿⣶⣾⣿⣿⣶⣾⣿⣿⣿⣿⣿⣿⡎⣿⣿⣿⣿ ")
        print(f"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿⡇⢸⡇⣿⣿⣿⣿ ")
        print(f"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢹⣿⣿⣿⣿⣿⣬⣙⢻⣿⣿⣿⣿⣿⡃⠄⢹⣧⣾⡷⢄⣿⣿⣿ ")
        print(f"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡉⢻⣿⣿⣿⣿⣗⠨⣿⣿⣿⣿⣿⣷⣼⣿⡿⠟⢫⣾⣿⣿⣿ ")
        print(f"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡌⠛⢁⣉⡉⢤⣤⣿⠋⠈⢉⣉⣍⣵⣶⣾⣿⣿⣿⣿⣿ ")
        print(f"⣯⡄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣾⣿⠏⠄⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ")
        print(f"⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣈⣉⣀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿ ")

        time.sleep(t)
        clear_console()
        if i == 2:
            # Muestra una imagen en ASCII art diferente
            print(f"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print(f"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print(f"⣿⣿⡟⢨⣯⣙⡛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print(f"⣿⣿⣿⢹⣿⣿⣿⣷⣦⣤⡙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print(f"⣿⣿⣿⡚⠟⠛⠿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⡉⠙⢛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print(f"⣿⣿⣿⣿⣿⣿⣷⣶⡆⢸⠣⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠉⠉⠁⣠⣬⣙⣓⠂⠉⠻⠿⠿⢿⣿⣿⣿⣿⣿⣿")
        print(f" ⣿⣿⣿⣿⣿⣿⣿⣿⠸⠷⠶⡄⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠷⢂⢈⡛⠿⢿⣿⣶⣿⣿⣿⣶⣌⢻⣿⣿⣿⣿")
        print(f"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠛⠛⣻⣿⣿⡿⠋⠁⣵⣶⠀⢰⣿⣿⣿⣿⣶⣾⣿⣿⣿⣿⡟⣙⡆⢿⣿⣿⣿")
        print(f"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⡆⠁⠹⠿⢟⣵⣀⠐⣻⣿⣆⣬⣿⣿⣿⣿⣿⣿⣿⡿⠛⢻⣷⣴⣧⡙⣿⣿⣿")
        print(f"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⢢⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡈⢤⣿⣿⣟⢃⣿⣿⣿")
        print(f"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⠿⢉⣡⣿⣿⣿⣿")
        print(f"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡜⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡿⠿⢿⣿⣇⠀⣦⢰⣾⣿⣿⣿⣿⣿⣿")
        print(f"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠻⣿⣿⣿⣿⣯⠉⣡⣴⣾⣶⣮⢻⣿⠃⣢⣿⣿⣿⣿⣿⣿⣿⣿")
        print(f"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠜⠛⢿⡿⠟⣰⣿⣿⣿⣿⣿⣆⣉⣰⣿⣿⣿⣿⣿⣿⡿⡿⣿")
        print(f"⣿⢿⢿⡿⡿⣿⡿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣌⣓⣒⣙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⢟⣼")

        time.sleep(t)
        clear_console()
        if i == 3:
            # Muestra otra imagen en ASCII art
            print(f"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣼⣿⣿⣿⣿ ")
        print(f"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ")
        print(f"⣿⠅⣮⣭⡛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ")
        print(f"⣿⢌⣿⣿⣿⣷⣶⣬⣝⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ")
        print(f"⣿⡆⢻⣿⠿⣿⣿⣿⣿⢣⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⠀⣀⡀⠀⠥⠌⡙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print(f"⣿⣿⣶⣶⣶⣶⡖⢠⣇⣘⣋⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⡈⠛⠿⣿⣷⣶⣤⣠⣭⣝⣛⡛⢿⣿⣿⣿⣿ ")
        print(f"⣿⣿⣿⣿⣿⣿⣇⣜⣛⡛⠻⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢟⣒⣤⣭⣹⣿⣿⣿⣿⣿⣿⣦⢻⣿⣿⣿ ")
        print(f"⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠈⠉⢉⣽⣿⣿⠟⠛⣭⣍⣤⡆⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠨⣿⡁⣿⣿⣿⣿")
        print(f"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⠐⠈⠛⣫⣤⡀⠐⣹⣿⣿⣧⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡟⢉⠙⣶⣿⣿⠈⣿⣿ ")
        print(f"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡶⢰⣿⣿⣷⣄⣾⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⠿⣿⣷⣂⣬⣿⣿⠖⣰⣿⣿ ")
        print(f"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢣⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣉⠙⢉⣄⡘⢿⣿⣿ ")
        print(f"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⠟⢉⢛⡛⠛⢿⣿⠿⡿⣷⠈⣵⣿⣿⣿ ")
        print(f"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣸⣿⣿⣿⣿⣿⠿⠟⠛⠙⣋⣡⣶⣶⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿ ")
        print(f"⣟⣟⢿⣿⣿⣿⣿⣿⣿⣿⣿⠃⣼⢟⡻⠿⢟⣋⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ")
        print(f"⡿⣧⢹⣿⣿⣿⣿⣿⣿⣿⣿⠘⢢⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ")
        print(f"⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ")

        time.sleep(t)
        clear_console()
        if i == 4:
            # Muestra otra imagen en ASCII art diferente
            print(f"⣿⣿⣧⣿⣧⣿⣼⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣥⣯⣿")
        print(f"⣿⣯⢠⣭⣍⣛⡛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print(f"⣿⣿⡆⣿⣿⣿⣿⣿⣶⣦⣍⡛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print(f"⣿⣿⡆⢹⣿⣿⣿⣿⣿⣿⡿⢱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print(f" ⣿⣿⣷⣶⣶⣶⣶⡶⣠⣧⣭⣭⢍⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print(f"⣿⣿⣿⣿⣿⣿⣿⣿⣧⣬⣤⡆⢉⠈⠛⢻⣿⣿⣿⣿⣿⣿⣿⡟⠋⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print(f"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣤⡖⠀⠚⢛⣋⣭⠀⠤⣭⡄⠀⠀⢤⣑⣢⠌⣛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print(f" ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢖⣰⣿⣿⣟⠠⣸⣿⣿⠀⠀⠸⣿⣿⣷⣤⣠⣬⣬⡙⠿⣿⣿⣿⣿⣿")
        print(f"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢏⣼⣿⣿⣿⣿⣷⣿⣿⣿⣌⣴⣷⣶⣽⣿⣿⣿⣿⣿⣿⣧⡜⣿⣿⣿⣿")
        print(f"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢽⡇⣽⣿⣿⣿")
        print(f"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣉⠹⣷⣾⣇⠈⣿⣿⣿")
        print(f"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆⣿⣿⣿⣿⠏⠻⠻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣀⣷⣿⣿⠏⣱⣿⣿⣿")
        print(f"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠘⡁⢠⣤⣶⣾⣿⣿⣿⣷⣶⣬⡻⣿⣿⣿⡘⠿⠿⠿⠟⢋⣥⣾⣿⣿⣿⣿")
        print(f"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡌⢻⣿⣇⠐⣆⢺⣿⣿⣿⣿⣿⣿⡿⢻")
        print(f"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⢻⣿⡀⠻⠇⣿⣿⣿⣿⣿⣟⣘⢘")
        print(f"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣷⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        time.sleep(t)
        clear_console()

    # Incrementa cont para que el bucle while pueda terminar eventualmente
    cont += 1
