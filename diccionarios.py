def run():
    # mi_diccionario = {
    #     'llave1': 1,
    #     'llave2': 2,
    #     'llave3': 3,
    # }

    # # print(mi_diccionario['llave1'])
    # # print(mi_diccionario['llave2'])
    # # print(mi_diccionario['llave3']) 

    poblacion_paises = {
         'Argentina': 44938712,
         'Brasil': 210147125,
         'Colombia': 50372424
     }

    # print(poblacion_paises['Bolivia'])

    # for pais in poblacion_paises.keys():
    #     print(pais)
    
    # for pais in poblacion_paises.values():
    #     print(pais)

    # for pais, poblacion in poblacion_paises.items():
    #     print(pais + ' tiene ' + str(poblacion) + ' habitantes')
    pais = input('¿De que pais deseas conocer sus habitantes?: ')
    pais = pais
    if pais == 'argentina' or pais == 'Argentina':
        print(poblacion_paises['Argentina'])
    elif pais == 'Brasil' or pais == 'brasil':
        print(poblacion_paises['Brasil'])
    elif pais == 'Colombia' or pais == 'colombia':
        print(poblacion_paises['Colombia'])
    else:
        print('No conocemos la poblacion de ese pais')


if __name__ == '__main__':
    run()