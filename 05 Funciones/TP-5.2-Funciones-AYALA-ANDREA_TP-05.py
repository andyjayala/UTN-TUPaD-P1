# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

# def hola_mundo():
#     print("Hola Mundo")

# hola_mundo()


# 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

# def saludar_usuario(nombre):
#     print(f"Hola {nombre}")

# saludar_usuario(nombre=input("Ingrese su nombre: "))

# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

# def informacion_personal(nombre, apellido, edad, residencia):
#     print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# informacion_personal(nombre=input("Ingrese su nombre: "), apellido=input("Ingrese su apellido: "), edad=input("Ingrese su edad: "), residencia=input("Ingrese su residencia: "))


# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_
# circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas
# funciones para mostrar los resultados.

# def calcular_area_circulo(radio):
#     return 3.14*radio*radio

# def calcular_perimetro_circulo(radio):
#     return 3.14*2*radio

# radio=int(input("Ingrese el radio: "))
# print(f"El área es {calcular_area_circulo(radio)} y el perímetro es {calcular_perimetro_circulo(radio)}")


# 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

# def segundos_a_horas(segundos):
#     horas = segundos // 3600
#     seg = segundos - (horas*3600)
#     print(f"Es/son {horas} hora/s con {seg} segundos")

# segundos_a_horas(segundos=int(input(f"Ingrese los segundos que se convertiran en horas: ")))


# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

# def tabla_multiplicar(numero):
#     for i in range (0,11):
#         print(f"{numero} x {i} = {numero * i}")

# tabla_multiplicar(int(input("Ingrese un número y le diremos la tabla: ")))


# 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado
# de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

# def operaciones_basicas(a, b):
    
#     print(f"La suma es: ",(a + b))
#     print(f"La resta es: ",(a - b))
#     print(f"La multiplicación es: ",(a * b))
        
#     if b != 0:   
#         print(f"La división es: ",(float(a / b)))
#     else:
#         print(f"No se puede dividir por 0")


# operaciones_basicas(int(input("Ingrese un número entero: ")), int(input("Ingrese otro número entero: ")))


# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC)--> peso(kg)/m^2. Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

# def calcular_imc (peso, altura):
#     imc = float(peso / (altura**2))
#     print(f"El IMC es: ", imc)

# calcular_imc(float(input("Ingrese su peso en kilos: ")), float(input("Ingrese su altura en metros: ")))


# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. La fórmula es: F = (C * 9/5) + 32 // Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

# def celsius_a_fahrenheit(celsius):
#     fahrenheit = float((celsius * (9/5)) + 32)
#     print(f"{celsius} grados Celsius son equivalentes a {fahrenheit} grados Fahrenheit")

# celsius_a_fahrenheit(float(input("Ingrese la temperatura en grados Celsius: ")))


# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. 
# Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a, b, c):
    prom = (a + b + c) / 3
    print(f"El promedio es ", prom)

calcular_promedio(float(input("Ingrese un número entero: ")), float(input("Ingrese otro número entero: ")), float(input("Ingrese un tercer número entero: ")))
