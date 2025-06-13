# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para 
# calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario

# def factorial(num):
#     if num == 0:
#         return 1
#     else:
#         return factorial(num-1) * num

# num = int(input("Ingrese número entero: "))
# for i in range (num+1):
#     print(f"Factorial de",i, "es", factorial(i))


# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra
#  la serie completa hasta la posición que el usuario especifique.

# def fibonacci(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return fibonacci(num-1) + fibonacci (num-2)

# num = int(input("Ingrese un número: "))    
# for i in range(num +1):
#     print(fibonacci(i))
    
    

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). 
# Prueba esta función en un algoritmo general.

# def potencia(n,m):
#     if m > 1:
#         return n * potencia(n,(m-1))
#     else:
#         return n

    
# print(f"El resultado es:", potencia(int(input("Ingrese la base: ")), int(input("Ingrese la potencia: "))))


# 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario 
# como una cadena de texto.
# Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este procedimiento:
# 1. Dividir el número por 2.
# 2. Guardar el resto (0 o 1).
# 3. Repetir el proceso con el cociente hasta que llegue a 0.
# 4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario
# Ejemplo:
# Convertir el número 10 a binario:
# 10 ÷ 2 = 5 resto: 0
# 5 ÷ 2 = 2 resto: 1
# 2 ÷ 2 = 1 resto: 0
# 1 ÷ 2 = 0 resto: 1
# Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010".


# def binario(x):
#     if x == 0:
#         return ""
#     else:
#         return binario(x // 2) + str(x % 2)
    
# print(f"El binario es: ", binario(int(input("Ingrese el numero: "))))

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva 
# True si es un palíndromo o False si no lo es.
# Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().

# def es_palindromo(palabra):
#   if len(palabra) < 2:
#     return True
#   if palabra[0] == palabra[-1]:
#     return es_palindromo(palabra[1:-1])
#   else:
#     return False
  
# palabra = input("Ingresá tu palabra: ")

# print ("Es palíndromo") if es_palindromo(palabra) else print("No es palíndromo")


# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos 
# sus dígitos.
# Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)

# def suma_digitos(n):
#     if n == 0:
#         return 0
#     else:
#         return n + suma_digitos(n-1)
    
# print(f"El resultado es:", suma_digitos(int(input("Ingrese el numero: "))))

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), 
#  así sucesivamente hasta llegar al último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de 
# bloques que necesita para construir toda la pirámide.
# Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)

# def contar_bloques(n):
#     if n == 1:
#         return 1
#     else:
#         return n + contar_bloques(n - 1)
    
# print(f"El número de bloques necesario es: ", contar_bloques(int(input("Ingrese el numero de bloques colocados: "))))

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito 
# (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.
# Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4
# contar_digito(123456, 7) → 0

## Aclaración: Vi este ejercicio con una compañera porque no me salía

# def contar_digito(numero, digito):
#     if numero == 0:
#       return 0
#     if numero % 10 == digito:
#       return 1 + contar_digito(numero // 10, digito)
#     else:
#       return 0 + contar_digito(numero // 10, digito)
    
# numero_entero_positivo = int(input("Ingresá un número entero positivo: "))
# digito = int(input("Ingresá un digito del 0 al 9: "))

# if numero_entero_positivo < 0 or digito > 9 or digito < 0:
#     print("Número o digito incorrecto")
# else:
#     print(f"Aparece {contar_digito(numero_entero_positivo, digito)} veces")