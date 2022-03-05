def recorrer_cadena():
    cadena = input("Ingresa la cadena: ")
    cadena2 = ""
    for caracter in cadena:
        cadena2 += caracter * 2
    print("cadena = ", cadena[::-1])
    print("cadena2 =", cadena2)

if __name__ == "__main__":
    recorrer_cadena()