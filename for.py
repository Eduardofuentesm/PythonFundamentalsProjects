# FORMA 1 SEGUN YO, DE COMO HACER UNA TABLA BASICA DE MULTIPLICAR DE CUALQUIER NUMERO CON UN LIMITE QUE TU DEFINES
tabla = int(input('¿Que número deseas multiplicar?: '))
tabla_2 = int(input('¿Hasta que numero deseas multiplicarlo?: '))

for numero in range(0, tabla_2):
    numero = numero+1
    multiplicacion = numero * tabla
    print(str(tabla)+ " * " + str(numero) + " = " + str(multiplicacion))

# SEGUNDA FORMA SEGUN YO, DE COMO HACER UNA TABLA BASICA DE MULTIPLICAR EN MENOS LINEAS, IGUAL TU DECIDES EL LIMITE
table = float(input('¿Qué tabla deseas saber?: '))
limit = int(input('¿Cual sera el limite de la tabla?: '))
print('\n'.join([f'{i} * {int(++table)} = {int(table*i)}'for i in range(1, limit+1)]))