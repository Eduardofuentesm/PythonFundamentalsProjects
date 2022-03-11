# Author: Eduardo Fuentes
import os
import sys
import time


def conversor_divisa(tipo_moneda, valor_dolar):
    os.system('clear')
    moneda = input('Cuantos Dolares US$  deseas convertir a ' + tipo_moneda+ ': ')
    moneda = float(moneda)
    dolares = moneda * valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    time.sleep(2)
    os.system('clear')
    print('Tienes ' + tipo_moneda + dolares)
    time.sleep(2)
    os.system('clear')
    nuevo_intento = input('¿Deseas hacer nueva conversion?: (s/n): ')
    if nuevo_intento == 's' or nuevo_intento == 'S':
        os.system('clear')
        run()
    else:
        os.system('clear')
        print('\n\tHasta la vista Inteligente programador de python')
        time.sleep(2)
        os.system('clear')
        sys.exit()


def run():
    os.system('clear')
    print('**¡Bienvenido al conversor de divisas!**\n\n')
    time.sleep(2)
    os.system('clear')
    print('Convertir de dolares a: \n')
    divisas = """

        1 - Euros
        2 - Quetzales
        3 - Pesos Argentinos
        4 - Pesos Colombianos
        5 - Pesos Mexicanos
        6 - Salir del conversor

        Elige una divisa:  """

    opciones = int(input(divisas))
            
    if opciones == 1:
        conversor_divisa('Euros €', 0.91)
    elif opciones == 2:
        conversor_divisa('Quetzales Q', 7.75)
    elif opciones == 3:
        conversor_divisa('Pesos Argentinos ARP$a', 108.56)
    elif opciones == 4:
        conversor_divisa('Pesos Colombianos COL$', 3777.50)
    elif opciones == 5:
         conversor_divisa('Pesos Mexicanos $', 20.95)
    elif opciones == 6:
        os.system('clear')
        print('\n\tHasta la vista Inteligente programador de python')
        time.sleep(2)
        os.system('clear')
        sys.exit()
    else:
        os.system('clear')
        print('\n\tIngrese una opcion valida por favor')
        time.sleep(2)
        os.system('clear')
        run()
        
    
 
if __name__ == "__main__":
    run()