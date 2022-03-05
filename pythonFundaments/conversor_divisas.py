def run():
    print('**¡Bienvenido al conversor de divisas!**\n\n')
    print('Convertir de dolares a: \n')
    divisas = {

        'Euros': 1,
        'Quetzales': 3,
        'Pesos Argentinos': 4,
        'Pesos Colombianos': 5,
        'Pesos Mexicanos': 6,
    }
    for opciones in divisas.keys():
        print(opciones)


# def  run():
#     print('**¡Bienvenido al conversor de divisas!**')
#     moneda = int(input('¿Cuantos Dolares deseas cambiar?: ' ))
#     moneda = int(moneda)

    
if __name__ == "__main__":
    run()