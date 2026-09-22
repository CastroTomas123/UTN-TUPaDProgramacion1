print("-" * 40)

print("Primera Actividad")

print("-" * 40)

# Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

print("-" * 40)

print("Segunda Actividad")

print("-" * 40)

# Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

saludar_usuario("Tomas")

print("-" * 40)

print("Tercera Actividad")

print("-" * 40)

# Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

nombre = input("Pon tu nombre: ")
apellido = input("Pon tu apellido: ")
edad = int(input("Pon tu edad: "))
residencia = input("Pon donde vives: ")

# Pedimos datos primero y despues defino funcion

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

informacion_personal(nombre, apellido, edad, residencia)

print("-" * 40)

print("Cuarta Actividad")

print("-" * 40)

# Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro 
# y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

def calcular_area_circulo(radio):
    return 3.14 * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * 3.14 * radio

radio_usuario = float(input("Cual es el radio de su circulo?(en cm): "))

area = calcular_area_circulo(radio_usuario)
perimetro = calcular_perimetro_circulo(radio_usuario)

print(f"El area de su circulo es: {area:.2f}cm2")
print(f"El perimetro del circulo es: {perimetro:.2f}cm")

print("-" * 40)

print("Quinta Actividad")

print("-" * 40)

# Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    return segundos / 60 / 60

segundos_usuario = int(input("Cuantos segundos quiere pasar a horas?: "))

hora = segundos_a_horas(segundos_usuario)

print(f"Los segundos en horas son: {hora:.2f}h")

print("-" * 40)

print("Sexta Actividad")

print("-" * 40)

# Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{i} x {numero} = {i * numero}")

numero = int(input("Ingrese un numero: "))

tabla_multiplicar(numero)

print("-" * 40)

print("Septima Actividad")

print("-" * 40)

# Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    division = a / b
    multiplicacion = a * b
    return suma, resta, division, multiplicacion

a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))

suma, resta, division, multiplicacion = operaciones_basicas(a, b)

print(f"La suma entre esos numeros es: {suma}\nLa resta entre esos numeros es: {resta}\nLa division entre esos numeros es: {division:.2f}\nLa multiplicacion entre esos numeros es: {multiplicacion:.2f}")

print("-" * 40)

print("Octava Actividad")

print("-" * 40)

# Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales

def calcular_imc(peso, altura):
    IMC = peso / (altura ** 2)
    return IMC

peso = float(input("Indique su peso en kg: "))
altura = float(input("Indique su altura en m: "))

resultado_imc = calcular_imc(peso, altura)

print(f"Su IMC es de: {resultado_imc:.2f}")

print("-" * 40)

print("Novena Actividad")

print("-" * 40)

# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función

def celsius_a_fahrenheit(celsius):
    return (celsius * 1.8) + 32

grados_celsius = float(input("Indique la temperatura en grados celsius: "))

print(f"Los grados celsius pasados a fahrenheit son: {celsius_a_fahrenheit(grados_celsius)}°F")

print("-" * 40)

print("Decima Actividad")

print("-" * 40)

# Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Ingrese un numero: "))
b = float(input("Ingrese otro numero: "))
c = float(input("Ingrese otro numero: "))

print(f"El promedio de esos numeros es: {calcular_promedio(a, b, c):.2f}")