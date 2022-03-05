def conversor(tipo_moneda, valor_moneda):
    pass


def run():
    print('\n¿A que divisa deseas convertir?: \n')
    menu_divisas = float(input('Elige una opcion: '))
    menu_divisas = int(menu_divisas)
    
#1 menu principal
menu_principal = """ 
Bienvenido al conversor de monedas 😎💰
¿Qué divisa posees?: 

1 - Quetzales
2 - Pesos argentinos
3 - Pesos colombianos
4 - pesos mexicanos
5 - Dolares

Elige una opcion: """


opciones = int(input(menu_principal))


if __name__ == "__main__":
    run()