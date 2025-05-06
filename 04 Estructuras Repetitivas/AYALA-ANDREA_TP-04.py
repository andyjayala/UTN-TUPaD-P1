# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

# for i in range (0, 101):
#     print (i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

# # Opción 1: Lo primero que se me ocurrió fue en pensarlo como string y aplicar una función que evalúe el tamaño
# num = input("Ingrese un número entero: ")
# cantidad_de_cifras = len(num)

# print(f"El número contiene {cantidad_de_cifras} dígitos")

# # Opción 2: Sé que tenemos que aplicar bucles, así que planteé esta respuesta evaluando por posición a posición 
# # con un for:

# num = input("Ingrese un número entero: ")

# x = 0
# for i in num:
#    x = x + 1

# print(f"El número contiene {x} dígitos")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

# num =int(input("Ingrese el primer número: "))
# num_dos = int(input("Ingrese el segundo número: "))

# suma = 0
# for i in range (num+1, num_dos):
#     suma = suma + i

# print(f"La suma entre los números enteros comprendidos entre dos valores excluyendo esos dos valores es {suma}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

# num = int(input("Ingrese los números que desea sumar. Ingrese 0 cuando quiera detener el programa: "))

# suma = 0
# while (num != 0):
#     suma = suma + num
#     num = int(input("Ingrese los números que desea sumar. Ingrese 0 cuando quiera detener el programa: "))

# print(f"La suma de los números ingresados es {suma}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

# import random
# numero_azar = random.randint(0, 9)

# num = 10
# while numero_azar != num:
#     num = int(input("Adivine el número seleccionado al azar del 0 al 9: "))

# print(f"Correcto! El número era el {num}")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

# for i in range (100, -1, -2):
#     print (i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

# num = int(input("Ingrese un número entero positivo: "))

# suma = 0
# for i in range (0, num+1):
#     suma = suma + i

# print(f"La suma desde el 0 hasta el número ingresado es: {suma}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# contador = 0
# es_par = 0
# es_impar = 0
# es_positivo = 0
# es_negativo = 0
# cero = 0

# while contador != 100:
#     num = int(input("Ingrese 100 números enteros: "))
#     contador += 1
# 
#     if (num % 2 == 0):
#         es_par += 1
#     else:
#         es_impar += 1
# 
#     if (num > 0):
#         es_positivo += 1
#     elif (num == 0):
#         cero += 1
#     else:
#         es_negativo += 1

# print(f"De los 100 números ingresados: {es_par} es/son par/es; {es_impar} es/son impar/es")
# print(f"De los cuales: {es_positivo} es/son positivo/s; {es_negativo} es/son negativo/s; y {cero} es/son cero/s")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

# contador = 0
# suma = 0

# while contador != 100:
#     num = int(input("Ingrese un número hasta llegar a 100: "))
#     contador += 1
#     suma = suma + num

# promedio = suma / 100

# print(f"La media (o promedio) entre los 100 números ingresados es {promedio}")


# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

# num = int(input("Ingrese un número para invertir: "))

# es_negativo = num < 0
# num_invertido = 0
# modulo = abs(num)

# while modulo > 0:
#     digito = modulo % 10
#     num_invertido = num_invertido * 10 + digito
#     modulo = modulo // 10

# if es_negativo:
#     num_invertido = -num_invertido

# print(f"El número invertido es: {num_invertido}")
