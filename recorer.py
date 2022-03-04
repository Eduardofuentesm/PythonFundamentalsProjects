def run():
     nombre = input("Escribe tu nombre: ")
     print("nombre = ", nombre[::-1])
     for letra in nombre:
         print(letra)
     frase = input("Escribe una frase: ")
     print("frase = ", frase[::-1])
     for letritas in frase:
        print(letritas.upper())

if __name__ == "__main__":
    run()