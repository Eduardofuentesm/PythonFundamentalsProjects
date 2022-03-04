nombre = input("¿Cual es tu nombre? \n")  # Le pide al usuario que ingrese su numero
print("Hola " + nombre )  # Imprime "Hola y el nombre que el usuario haya ingresado"
ok = 1 # Variable con la opcion adicional para convertir los dolares a quetzales
quetzales = input("¿Cuantos Quetzales tienes?: \n")  # variable que contiene la cantidad de quetzales que el usuario tiene
quetzales = float(quetzales) # Convierte lo ingresa en numeros con decimal
valor_dolar = 7.5 # variable con un valor definido, el cual es el valor del cambio de $1 = Q7.5
convertir_a_dolares = quetzales / valor_dolar # Operacion para convertir la cantidad de quetzales del usuario a dolares, dividiendo la cantidad de quetzales / el valor del dolar
convertir_a_dolares = str(round(convertir_a_dolares, 2))  # La variable "convertir_a_dolares" contiene en caracteres (str) y redondea (round) los decimales de la operacion "convertir_a_dolares" en dos decimales unicamente
print("Tienes  $" + convertir_a_dolares + " dólares")  # Imprime "Tienes $(resultado de operacion) dolares"
print("¿convertir dolares a quetzales?")  # Imprime una nueva opcion, pregunta si el usuario ahora desea convertir nuevamente a quetzales
respuesta = input("presiona 1 (ok)\n")  # la Variable "respuesta" contiene la opcion (unica) que se le brinda al usuario
dolares = input("¿Cuantos dolares deseas convertir?: \n") # al precionar 1 , le pedira al usuario que ingrese la cantidad de dolares que desee convertir
dolares = float(dolares) # convierte la cantidad ingresada en numeros reales (con decimal)
convertir_a_quetzlaes = dolares * valor_dolar # Realiza la operacion ahora multiplicando la cantidad de dolares que desea convertir el usuario * el valor del dolar
convertir_a_quetzlaes = str(round(convertir_a_quetzlaes, 2)) # La variable "convertir_a_quetzales" contiene en caracteres (str) y redondea en 2 decimales el valor de la operacion.
print("Tienes Q" + convertir_a_quetzlaes + "quetzales")  # Le imprime al usuario el resultado de la cantidad de quetzales que tiene al convertir sus dolares