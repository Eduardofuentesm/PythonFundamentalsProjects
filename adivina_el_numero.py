import random
import os
import sys
import time

def menu():
    nuevo_intento = input('¿Deseas volver a jugar?: (s/n): ')
    if nuevo_intento == 's':
        os.system('clear')
        run()
    else:
        sys.exit()

def run():
    vidas = 7
    numero_aleatorio = random.randint(1, 100)
    print(f'Bienvenido!!!\nTienes {vidas} intentos \n')
    numero_elegido = int(input("Elige un numero del 1 al 100: "))
    while numero_elegido != numero_aleatorio and vidas > 0:
        if numero_elegido < numero_aleatorio:
            os.system('clear')
            print("Busca un numero mas grande \n")
            time.sleep(2)
            os.system('clear')
        else:
            os.system('clear')
            print("Busca un numero mas pequeño \n")
            time.sleep(2)
            os.system('clear')
        vidas -= 1
        print(f'**** Tienes {vidas} intentos **** \n')
        numero_elegido = int(input("Eligre otro numero: \n"))
    if vidas == 0:
        print(f'No has tenido tanta suerte amigo // El numero correcto era {numero_aleatorio} ')
        time.sleep(2)
        os.system('clear')
        menu()
    else:
        print("¡Ganaste!")
        time.sleep(2)
        os.system('clear')
        menu()


if __name__ == "__main__":
    run()