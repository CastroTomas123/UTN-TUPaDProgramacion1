# Unidad 5

print("-" * 40)

print("Primera Actividad!")

print("-" * 40)

# Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

lista = []

# Creamos un for con los rangos establecidos

for i in range(0,101,4):

    lista.append(i)

# Le removemos el 0
lista.remove(0)
print(lista)

print("-" * 40)

print("Segunda Actividad!")

print("-" * 40)

# Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
# penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
# indexing con números negativos!

lista = [0, 100, True, "Argentina", "Fernet"]

# Accedo a la posicion 3, lo deduzco porque al contar todos los elementos que daria 5 la ultima posicion es siempre 1 menos y como el ejercicio pide el penultimo le resto 2

print(lista[len(lista) - 2])

print("-" * 40)

print("Tercera Actividad!")

print("-" * 40)

# Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla

lista_vacia = []

# Utilize un for para agregar 3 elementos diferentes

for i in range(3):
    lista.append(i)

print(lista_vacia)

print("-" * 40)

print("Cuarta Actividad!")

print("-" * 40)

# Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
# respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
# en los videos o bien investigar cómo funciona el indexing con números negativos!
# animales = ["perro", "gato", "conejo", "pez"]

animales = ["perro", "gato", "conejo", "pez"]

# Modifico directamente las posiciones por lo que me pide el ejercicio

animales[1], animales[3] = "loro", "oso"

print(animales)

print("-" * 40)

print("Quinta Actividad!")

print("-" * 40)

# Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

# Revisa dentro de la lista cual es el valor maximo y lo elimina directamente con remove

print("-" * 40)

print("Sexta Actividad!")

print("-" * 40)

# Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros

lista = []

# Con un bucle for creamos la lista

for i in range(10, 31, 5):
    lista.append(i)

# Muestro en pantalla los dos primeros elementos por el indice

print(f"Los dos primeros elementos son: {lista[0]}, {lista[1]}")

print("-" * 40)

print("Septima Actividad!")

print("-" * 40)

# Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
# cualquiera.
# autos = ["sedan", "polo", "suran", "gol"]

autos = ["sedan", "polo", "suran", "gol"]

# Hago lo mismo que el ejercicio 4

autos[1], autos[2] = "Fiat 1", "Reno 12"

print(autos)

print("-" * 40)

print("Octava Actividad!")

print("-" * 40)

# Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
# directamente. Imprimir la lista resultante por pantalla

dobles = []

# Con un for creamos la lista y añadimos los elementos que nos piden

for i in range(5,16,5):
    dobles.append(i*2)

print(dobles)

print("-" * 40)

print("Novena Actividad!")

print("-" * 40)

# Dada la lista “compras”, cuyos elementos representan los productos comprados por
# diferentes clientes:
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# Hacemos lo que nos pide cada actividad

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

# Imprimimos resultado

print(compras)

print("-" * 40)

print("Decima Actividad!")

print("-" * 40)

# Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.

lista_anidada = []

lista_anidada.append(15)
lista_anidada.append(True)
lista_anidada.append([25.5, 57.9, 30.6])
lista_anidada.append(False)

print(lista_anidada)
