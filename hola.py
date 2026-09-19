import math


print("Primera Actividad")

print("Hola Mundo")

print("Segunda Actividad")

nombre = input("Cual es tu nombre?: ")
print(f"Hola {nombre}")

print("Tercera Actividad")

nombre = input("Cual es tu nombre?: ")
apellido = input("Cual es tu apellido?: ")
lugar = input("En que pais vives?: ")
edad = int(input("Cual es tu edad?: "))
print(f"Hola soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}")

print("Cuarta Actividad")

a = float(input("Indica el radio del Circulo para calcular Perimetro y Area: "))
area = math.pi * a ** 2
perimetro = 2 * math.pi * a
print(f"El Perimetro es: {perimetro:.1f}cm y El Area es: {area:.1f}cm²")

print("Quinta Actividad")

b = float(input("Pon la cantidad de segundos que quieres pasar a horas: "))
hora = b / 3600
print(f"Son {hora:.2f} horas")

print("Sexta Actividad")

c = float(input("Indica un solo numero: "))
print(f"{c:.0f} x 1: {1 * c:.0f}\n{c:.0f} x 2: {2 * c:.0f}\n{c:.0f} x 3: {3 * c:.0f}\n{c:.0f} x 4: {4 * c:.0f}\n{c:.0f} x 5: {5 * c:.0f}\n{c:.0f} x 6: {6 * c:.0f}\n{c:.0f} x 7: {7 * c:.0f}\n{c:.0f} x 8: {8 * c:.0f}\n{c:.0f} x 9: {9 * c:.0f}\n{c:.0f} x 10: {10 * c:.0f}")

print("Septima Actividad")

d = float(input("Indica un solo numero: "))
e = float(input("Indica otro numero: "))
print(f"El resultado de sumarlos es {d + e}\nEl resultado de restarlos es {d - e}\nEl resultado de dividirlos es {d / e:.2f}\nEl resultado de multiplicarlos es {d * e:.2f}")

print("Octava Actividad")

peso = float(input("Indique su peso en kg: "))
altura = float(input("Indique su altura en cm: "))
f = altura / 100
print(f"Su indice de masa corporal es: {peso / f ** 2:.2f}")

print("Novena Actividad")

temperatura = float(input("Indique la temperatura en Grados Celcius: "))
print(f"La temperatura en Fahrenheit {9 / 5 * temperatura + 32:.2f}")
print("Decima Actividad")
g = float(input("Indique un solo numero: "))
h = float(input("Indique otro numero: "))
i = float(input("Indique otro numero: "))
j = g + h + i
print(f"El promedio entre estos tres numeros es: {j / 3:.2f}")