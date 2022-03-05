# def run():
#     # for contador in range(10):
#     #     if contador % 2 != 0:
#     #         continue
#     #     print(contador)

#     # for i in range(1000):
#     #     print(i)
#     #     if i == 624:
#     #         break

#     texto = input("Escribe un texto: ")
#     for letra in texto:
#         if letra == "o":
#             break
#         print(letra)

# if __name__ == "__main__":
#     run()

## -------------------------------------------------------------------------------------------
## -------------------------------------------------------------------------------------------

## BOHEMIAN RHAPSODY## 
# print('"Bohemia Rhapsody."', end='\n\n')

# for i in range(3):
#     if i == 0:
#         print('Oh')
#     if i == 2:
#         print('Mama mia, let me go.', end= '\n\n')
#         break
#     print('Mama mia,')

# print('Beelzebub has a  devil put aside')

# for i in range(3):
#     if i == 2:
#         print('For meeeeeee!')
#         break
#     print('For mee,')

## -------------------------------------------------------------------------------------------
## -------------------------------------------------------------------------------------------


# import random 

# Desayuno = ('Tamal con cafe', 'Huevos rancheros y jugo', 'Calentao y agua pura')
# def selectRandom(comida):
#   return random.choice(Desayuno)  

# Almuerzo = ('Bandeja paisa', 'Arroz con pollo', 'Ajiaco')
# def selectRandom(Almuerzo):
#   return random.choice(Almuerzo) 

# Cena = ('Hamburguesa', 'Arroz con pollo', 'Pizza')
# def selectRandom(Cena):
#   return random.choice(Cena) 

# def run():
 
#  while True:
#      opcion = (input( """Elige el tipo de comida: 
 
#      1. Desayuno
#      2. Almuerzo
#      3. Cena 
#       """))
 
#      if  opcion  == "1":

#          print('Haz seleccionado deayuno, El menu del día es: ', selectRandom(Desayuno) )
#          break

#      elif  opcion  == "2":

#          print('Haz seleccionado deayuno, El menu del día es: ', selectRandom(Almuerzo) )
#          break 
#      elif  opcion  == "3":
       
#          print('Haz seleccionado deayuno, El menu del día es: ', selectRandom(Cena) )
#          break 

#      elif opcion != (0, 3):
#          print ('Selecciona de nuevo')
#          continue

    

# if __name__ == '__main__':
#     run()

## -------------------------------------------------------------------------------------------
## -------------------------------------------------------------------------------------------

# numero = 0
# eleccion = int(input('Ingrese un numero: '))
# while numero < 10000:        
#         if numero == eleccion:
#             break
#         numero += 1 
#         if numero % 2 != 0:
#             continue
#         print(numero)

# contraseña = int(input('¿Cual es tu contraseña?: '))
# while contraseña != 24:
#     print ('no es tu contraseña')
#     break
# while contraseña == 24:
#     print('Bienvenido usuario')
#     break