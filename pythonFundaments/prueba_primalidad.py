def es_primo(numero):
    contador = 0

    for i in range(1, numero):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False

def run():
    numero = int(input("Escribe un numero: "))
    if numero == 1 or numero == 0:
        print('No es numero compuesto ni es numero primo \nbye amigo ')
    elif es_primo(numero):
        print(f"El numero {numero} Es primo")
    else:
        print(f"El numero {numero} es numero compuesto")

if __name__ == "__main__":
    run()