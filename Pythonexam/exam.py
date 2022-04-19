# PCEP - Programador de Python de Nivel Básico Certificado
# La certificación PCEP - Certified Entry-Level Python Programmer demuestra que la persona está familiarizada con los conceptos universales de la programación informática como los tipos de datos, los contenedores, las funciones, las condiciones, los bucles, así como la sintaxis del lenguaje de programación Python, la semántica y el entorno de ejecución.

# tup = (1, 1, 4, 8)
# tup = tup[-2:-1]
# tup = tup[-1]
# print(tup)


# dd = {"1": "0", "0": "1"}
# for x in dd.vals():
#     print(x, end="")

# i = 0
# while i < i + 2:
#     i += 1
#     print("*")
# else:
#     print("*")

# z = 0
# y = 10
# x = y < z and z > y or y > z and z < y
# print(x)

# def function_1(a):
#     return None

# def function_2(a):
#     return function_1(a) * function_1(a)

# print(function_2(2))

# x = float(input())
# y = float(input())
# print(y ** (1 / x))

# my_tuple = [1]
# my_tuple[1] = my_tuple [1] + my_tuple [0]

# dct = {'one': 'two', 'three': 'one', 'two': 'three'}
# v = dct['three']

# for k in range(len(dct)):
#     v = dct[v]

# print(v)

# lst = [i for i in range(-1, -2)]

# def fun(inp=2, out=3):
#     return inp * out

# print(fun(out=2))

# def func(a, b):
#     return b **a

# print(func(b=2, 2))

# print("a", "b", "c", sep="sep")

# lst = [[x for x in range(3)] for y in range(3)]

# for r in range(3):
#     for c in range(3):
#         if lst[r] [c] % 2 !=0:
#             print("#")

# def fun (x, y) :
#     if x == y:
#         return x
#     else:
#         return fun (x, y-1)
# print (fun (0, 3))

# my_list = [1, 2]

# for v in range(2):
#     my_list.insert(-1, my_list[v])

# print(my_list)

# foo = (1, 2 ,3)
# foo.index(0)

# x = 1 // 5 + 1 / 5
# print(x)

# y = input()
# x = input()
# print(x + y)

# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return 2

# print(fun(fun(2)))

# def fun(a, b, c=0):
#     print(fun)
#     # cuerpo de la funcion.

# a = 1
# b = 0
# a = a ^ b
# b = a ^ b
# a = a ^ b

# print(a, b)

# nums = [1, 2, 3]
# vals = nums
# del vals[:]
# print(vals)
# print(nums)

# nums = [1, 2, 3]
# vals = nums
# print(vals)
# print(nums)


# try:
#     print(5 / 0)
#     break
# except:
#     print("Lo siento, algo salio mal")
# except (ValueError, ZeroDivisionError):
#     print("mala suerte")

# dct = { }
# dct ['1'] = (1, 2)
# dct ['2'] = (2, 1)
# for x in dct.keys () :
#     print (dct [x] [1], end="")

# my_list = [x * x for x in range(5)]

# def fun (lst):
#     del lst[lst[2]]
#     return lst

# print(fun(my_list))

# x = 1
# y = 2
# x, y, z = x, x, y
# z, y, z = x, y, z

# print(x, y, z)

# x = int (input ())
# y = int (input ()) 
# x = x % y
# x = x % y
# y = y % x
# print (y)

# try:
#     value = input("Ingresa un valor: ")
#     print(int(value)/ len(value))
# except ValueError:
#     print("Entrada incorrecta...")
# except ZeroDivisionError:
#     print("Entrada erronea...")
# except TypeError:
#     print("entrada muy erronea...")
# except:
#     print("¡Buuu!")

# def find_mas(nums):
#     max_num = float("-inf")
#     for num in nums:
#         if num > max_num:
#             # num = max_num
#             # max_num = num
#             # max_num += 1
#             max_num += num

#     return max_num