def busqueda_binaria(lista, valor):
    steps = 0
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        steps +=1
        punto_medio = (izq+der) // 2

        if lista[punto_medio] == valor:
            return "valor encontrado en {} pasos, en la posición {}.".format(steps, punto_medio)
        if lista[punto_medio] > valor:
            der = punto_medio - 1
        if lista[punto_medio] < valor:
            izq = punto_medio + 1
    return "Elemento no encontrado"

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,20]

busqueda = busqueda_binaria(lista, 20)
print(busqueda)


# if __name__ == '__main__':
#     main()