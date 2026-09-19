import math
import statistics
import random

print("Primera Actividad")

edad = int(input("Cual es tu edad?: "))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print("Segunda Actividad")

nota = float(input("Indique la nota del examen del 1 al 10: "))
if 6 <= nota <= 10:
    print("Aprobado")
elif 0 <= nota < 6:
    print("Desaprobado")
else:
    print("Numero incorrecto, indicar del 1 al 10")

print("Tercera Actividad")

numero = int(input("Indique un número par: "))
numero1 = numero % 2
if numero1 == 0:
    print("Es un número par")
else:
    print("Por favor indique un número par")

print("Cuarta Actividad")

edad = int(input("Indique su edad: "))
match edad:
    case edad if 0 < edad < 12:
        print("Eres un niño")
    case edad if 12 <= edad < 18:
        print("Eres un adolescente")
    case edad if 18 <= edad < 30:
        print("Eres un adulto joven")
    case edad if edad >= 30:
        print("Eres un adulto")

print("Quinta Actividad")

contraseña = input("Indique una contraseña entre 8 y 14 caracteres: ")
if 8 <= len(contraseña) <= 14:
    print("Contraseña correcta")
else:
    print("Por favor ingrese una contraseña entre 8 y 14 caracteres")

print ("Sexta Actividad")

numeros_aleatorios = [random.randint(1,100) for i in range(50)]
media = statistics.mean(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
moda = statistics.mode(numeros_aleatorios)
print (f"Media = {media}\nMediana = {mediana}\nModa = {moda}\n")
if media > mediana > moda:
    print("Es Sesgo Positivo")
elif media == mediana == moda:
    print("Sin Sesgo")
else:
    print("Sesgo negativo")

print("Septima Actividad")

nombre = input("Indique su nombre o una frase: ")
if len(nombre) > 0 and nombre[-1].lower() in "aeiou":
    print(f"{nombre}!")
elif len(nombre) == 0:
    print("Por favor indique un nombre o frase")
else:
    pass

print("Octava Actividad")

nombre = input("Indique su nombre: ")
print("1 = Todo su nombre en mayusculas\n2 = Todo su nombre en minuscula\n3 = Su nombre con la primera letra mayuscula")
numero = int(input("Indique un numero del 1 al 3: "))
if numero == 1:
    print(nombre.upper())
elif numero == 2:
    print(nombre.lower())
elif numero == 3:
    print(nombre.title())
else:
    print("Por favor indique un numero del 1 al 3")

print("Novena Actividad")

terremoto = float(input("Indique la magnitud del terremoto segun la escala de Richter: "))
if 0 < terremoto < 3:
    print("Muy leve (Imperceptible)")
elif 3 <= terremoto < 4:
    print("Leve (Ligeramente Perceptible)")
elif 4 <= terremoto < 5:
    print("Moderado (Sentido por las personas, pero sin daños)")
elif 5 <= terremoto < 6:
    print("Fuerte (Causa daños en estructuras debiles)")
elif 6 <= terremoto < 7:
    print("Muy Fuerte (Causa daños significativos)")
elif 7 <= terremoto:
    print("Extremo (Puede causar daños a gran escala)")
else:
    print("Por favor escoja un numero arriba del 0")

print("Decima Actividad")

hemisferio = input("En cual hemisferio se encuentra? (Norte/Sur): ")
año = int(input("En que año esta?: "))
mes = int(input("En que mes esta?: "))
dia = int(input("En que dia esta?: "))
if (hemisferio.lower() == "sur") and ((mes == 12 and dia >= 21) or mes in (1,2)  or (mes == 3 and dia <= 20)):
    print("Estas en Verano!")
elif (hemisferio.lower() == "sur") and ((mes == 3 and dia >= 21) or mes in (4,5) or (mes == 6 and dia <= 20)):
    print("Estas en Otoño!")
elif (hemisferio.lower() == "sur") and ((mes == 6 and dia >= 21) or mes in (7,8) or (mes == 9 and dia <= 20)):
    print("Estas en Invierno!")
elif (hemisferio.lower() == "sur") and ((mes == 9 and dia >= 21) or mes in (10,11) or (mes == 12 and dia <= 20)):
    print("Estas en Primavera!")
elif (hemisferio.lower() == "norte") and ((mes == 12 and dia >= 21) or mes in (1,2) or (mes == 3 and dia <= 20)):
    print("Estas en Invierno!")
elif (hemisferio.lower() == "norte") and ((mes == 3 and dia >= 21) or mes in (4,5) or (mes == 6 and dia <= 20)):
    print("Estas en Primavera!")
elif (hemisferio.lower() == "norte") and ((mes == 6 and dia >= 21) or mes in (7,8) or (mes == 9 and dia <= 20)):
    print("Estas en Verano!")
elif (hemisferio.lower() == "norte") and ((mes == 9 and dia >= 21) or mes in (10,11) or (mes == 12 and dia <= 20)):
    print("Estas en Otoño!")
else:
    pass