import random

# La consigna de la primera actividad es que imprimamos del 0 al 100 incluido los dos extremos
print("Primera Actividad")
print("---------------------------------------------------------------------------------")
# En esta unidad y en la 4 voy a poner separadores entre actividades asi se ve mejor

for num in range (101):
    print(f"{num}")
# Como me pídieron que imprima del 0 al 100 vamos a usar el bucle for porque ya se la cantidad de veces que lo voy a usar
# Pongo in range 101 porque como el bucle for comienza desde el 0 ya toma un extremo y el 101 no incluye al rango entonces va a imprimir hasta el 100
print("---------------------------------------------------------------------------------")

print("Segunda Actividad")

print("A continuacion ingrese un numero entero para determinar la cantidad de digitos")

# La segunda actividad nos pide hacer un programa que solicite un numero entero y determine la cantidad de digitos

entero = int(input("Ingrese un numero entero: "))
# Primeramente le pedimos al usuario que ingrese un entero

if entero < 0:
    entero = abs(entero)
# Esto lo pongo en caso de que el usuario ingrese un numero negativo lo convierta a positivo porque en esta actividad solo precisamos saber cantidad de digitos no sumar ni nada

cont = 1
# Seteamos el contador a 1 para que en caso de que el usuario ponga 0 diga que es un numero de un digito

while entero != 0:
# Como la operacion del entero // 10 una vez que lo repetis reiteradas veces da 0 entonces usamos esto como condicion ya que si pone el usuario 0 no se ejecuta

    if entero >= 10:
        entero = entero // 10
        cont += 1
# Pongo el if que si es mayor o igual a 10 haga la operacion de entero // 10 asi le vamos quitando digitos y sumandolo en el contador
# Como al principio contamos el contador como 1 porque si o si tiene que poner un digito, si es mayor o igual a 10 estariamos sumandole otro digito y asi sucesivamente

    elif entero < 10:
        break
# Aca en caso de que el usuario ponga 9, 7 o cualquier digito debajo de 10 y arriba de -10 como sabemos que no es necesario seguir con el bucle lo cortamos ya que tenemos contabilizado el primer digito

print(f"Tu numero contiene {cont} digitos")

# Imprimimos el numero de digitos

# PD IMPORTANTE: Este ejercicio se puede hacer sin el if y el elif, lo consulte con ia pero esta es mi solucion pensandolo yo mismo. se puede arrancar con el cont en 0 y al principio agregarle al if un elif == 0
# PD IMPORTANTE:Ahi sabemos que directamente tiene un digito entonces sumamos un digito y listo pero bueno esta es mi solucion pensada por mi.

print("---------------------------------------------------------------------------------")

print("Tercera Actividad")

# La tercera actividad me dice que haga un programa que ponga dos valores enteros, entonces sume todos los numeros enteros entre si menos los dos valores enteros que pusieron
# Lo primero que voy a hacer es asignarle variables a los numeros y detectar numero mayor y menor

suma = 0
numero_mayor = 0
numero_menor = 0

# Asignamos variables, no va a haber ningun problema porque como valen 0 vamos a detectar si los valores de numero mayor y menor son iguales imprima que pongamos dos valores diferentes

print("A continuacion ponga dos numeros enteros para sumar todos los enteros entre si")

numero1 = int(input("Ingrese un numero entero: "))

numero2 = int(input("Ingrese otro numero entero: "))

# Luego de preguntarle los numeros vamos a crear un if que detecte si son iguales que ponga dos numeros diferentes
# Sino son iguales ver cual es menor y mayor

if numero1 == numero2:
    print("Deberias poner dos numeros diferentes")
else:
    if numero1 > numero2:
        numero_menor = numero2
        numero_mayor = numero1
    elif numero1 < numero2:
        numero_menor = numero1
        numero_mayor = numero2

# Como ya nos fijamos que no son iguales los numeros con el if podemos hacer esto para identificar cual es el menor y el mayor

    for numero in range (numero_menor + 1,numero_mayor):

# Porque al numero menor le pongo +1 y al numero mayor nada?
# La respuesta es simple el range incluye el inicio pero no el final entonces al numero menor le sumamos 1 y el numero mayor lo dejamos como esta

        suma += numero
    print(f"La suma es {suma}")

# Por ultimo imprimimos la suma

print("---------------------------------------------------------------------------------")

print("Cuarta Actividad")

# En esta actividad nos piden elaborar un programa que le pida al usuario ingresar numeros enteros y sumarlos secuencialmente.
# Que se corte cuando el usuario ponga 0, es bastante facil fabricarlo con while, ya que tenemos la condicion que siempre es true

suma = 0

# Le asignamos a la variable "suma" un valor para que empiece a contar

print("A continuacion pon los numeros enteros que quieras sumar secuencialmente")

# Le explicamos al usuario lo que tiene que poner

numero = int(input("Ingrese un numero entero (Ponga cero si quiere parar): "))

# Una vez ingresado el numero podemos empezar con el while

while numero != 0:
    suma += numero
    numero = int(input("Ingrese un numero entero (Ponga cero si quiere parar): "))

print(f"La suma es: {suma}")

# Ponemos la condicion el usuario pueda hacer el bucle hasta que el lo requiera y al momento de que el usuario ponga 0 corta automaticamente el bucle.
# Puse primero la suma para que sume y despues que ingrese el numero porque si llega a poner 0, ya habra contado el numero anterior para la suma.
# Luego imprimir el resultado de la suma.

print("---------------------------------------------------------------------------------")

print("Quinta Actividad")

print("Juega a adivinar el numero secreto!")

# En esta actividad nos piden que creemos un juego en que el usuario adivine un numero aleatorio del 0 al 9 y cuando adivine el numero ponga cuantos intentos le llevo
# Entonces al principio del archivo vamos a importar el random para crear ese numero aleatorio
# A continuacion lo que vamos a hacer es crear el numero secreto o random
# Tambien crearemos la variable del numero user

numero_secreto = random.randint(0,9)
numero_user = None

# Creamos la variable cont para contabilizar los intentos

cont = 0

# A continuacion comparamos los numeros con el while, el bucle se ejecuta hasta que el usuario adivine el numero

while numero_secreto != numero_user:
    numero_user = int(input("Ingrese un numero del 0 al 9 para adivinar el numero secreto: "))
    if 0 <= numero_user <= 9:
        cont += 1
    else:
        print("Es solo ingresar numero del 0 al 9")
print(f"El numero de intentos que le llevo son: {cont}")

# Primero lo que hacemos es que el usuario introduzca el numero pedido
# Luego lo que hacemos es verificar con if si el usuario puso los numeros dentro de lo pedido osea, del 0 al 9 sino se le pedira que ponga otro numero y se le dara la advertencia
# Luego dentro del if se contabiliza el intento y despues de que termine el bucle se imprime el numero

print("---------------------------------------------------------------------------------")

print("Sexta Actividad")

# Aca nos piden que hagamos un programa que ponga los numeros pares del 100 a 0 en orden decreciente

for num in range (100,-1,-2):
    print(f"{num}")

# No mucho que explicar solo puse que iniciara en el numero 100, luego que terminara en el -1 asi toma el 0
# Luego solo puse el paso en -2 y asi disminuye de 2 en 2
# Asi haciendo de 0 y 100 en orden decreciente

print("---------------------------------------------------------------------------------")

print("Septima Actividad")

# En esta actividad hay que hacer un programa que calcule la suma entre los numeros comprendidos entre 0 y un numero entero positivo que lo indique el usuario

# Empezamos sabiendo el inicio, con el numero indicado sabemos el final entonces usaremos for

print("A continuacion indique un numero entero positivo para calcular la suma entre los numeros entre 0 y el numero indicado")

numero_user = int(input("Ingrese un numero entero positivo: "))

# Le pedimos al usuario que ingrese el numero

suma = 0

# Le damos valor a la suma asi puede empezar a contar

if numero_user > 0:
    for num in range (0,numero_user + 1):
        suma += num
    print(f"La suma entre los numeros es: {suma}")
else:
    print("Solo un numero entero positivo")

# Usamos el if para verificar que sea un numero entero positivo y asi no errarle
# En el rango ponemos (0,numero_user + 1) al final le sumamos uno para que el numero que haya puesto el usuario cuente para la suma porque en el range el numero final no es tomado en cuenta
# Luego imprimimos el resultado

print("---------------------------------------------------------------------------------")

print("Octava Actividad")

print("A continuacion ingrese 100 numeros enteros asi clasificamos entre pares, impares, positivos y negativos")

# La actividad consiste en pedirle al usuario 100 numeros enteros y despues clasificarlos en numeros pares, impares, positivos y negativos.

# Aca vamos a usar for porque ya sabemos que hacer

cantidad_num = 100

# Ponemos esta variable para poder modificar el numero de numeros que ponga el usuario

cont_par = 0
cont_impar = 0
cont_positivo = 0
cont_negativo = 0

# Ponemos contador para cada tipo de numero

# Empezamos con el for poniendo el inicio y la variable de numeros que queremos poner

for numero in range (1,cantidad_num + 1):
    num = int(input("Ingrese un numero entero: "))
# Le pedimos al usuario que ingrese el numero
    if num != 0:
# Aca vamos a contar los positivos y negativos, como el 0 no cuenta ni como positivo ni negativo le decimos que si el numero puesto es distinto de 0 ahi empiece a contar
        if num > 0:
            cont_positivo += 1
        elif num < 0:
            cont_negativo += 1
    if num % 2 == 0:
        cont_par += 1
    else:
        cont_impar += 1
# Aca esta los contadores pares e impares, usamos la formula para saber el resto y si el resto da 0 es par y si da 1 es impar entonces ya sabemos
# Y ya solo nos queda imprimir los resultados

print(f"La cantidad de numeros pares = {cont_par}\nLa cantidad de numeros impares = {cont_impar}\nLa cantidad de numeros positivos = {cont_positivo}\nLa cantidad de numeros negativos = {cont_negativo}")

# Voy a expresar todo en una sola linea para no repetir varias veces el print.

print("---------------------------------------------------------------------------------")

print("Novena Actividad")

print("A continuacion ingrese 100 numeros enteros para calcular la media entre estos numeros")

# La actividad consiste en elaborar el programa que una vez que el usuario ingrese 100 numeros enteros, calcule la media entre estos numeros.

# Empezamos con la variables de la suma y la cantidad de numeros para poder facilmente cambiar

cantidad_numeros = 100
suma = 0

# Luego ponemos el for y que vaya sumando los numeros

for num in range (1,cantidad_numeros + 1):
    numeros = int(input("Ingrese un numero entero: "))
    suma += numeros

# Hacemos la cuenta de la media

media = suma / cantidad_numeros

# Imprimimos el resultado

print(f"La media entre estos numeros es: {media}")

print("---------------------------------------------------------------------------------")

print("Decima Actividad")

# La actividad consiste en hacer un programa donde le pida al usuario un numero entero y invirtamos los digitos por ejemplo 453 el resultado 354

print("Ponga un numero entero para invertir los digitos")

numero = int(input("Ingrese un numero entero: "))

# Le pedimos al usuario que ingrese el numero entero

numero = abs(numero)

# Ponemos abs en caso de que el numero que sea negativo lo convertimos en positivo ya que aca no importa tampoco si es negativo

num_invertido = 0

# Le damos valor al numero invertido y a continuacion crearemos el bucle while

while numero != 0:
    ult_digito = numero % 10
    num_invertido = num_invertido * 10 + ult_digito
    numero = numero // 10

# El bucle consiste en dif operaciones matematicas.
# Basicamente lo primero es para guardar el ultimo digito que cualquier numero % 10 da como resultado el ultimo digito
# Luego lo agregamos al numero invertido multiplicado por 10 + el ultimo digito (Mas adelante lo explico)
# Por ultimo borramos el ultimo digito haciendo // 10
# Cuando sea un numero de 2 o mas digitos al ya guardar el ultimo digito lo tenemos en el numero invertido. Entonces cuando ya borremos ese ultimo digito se reinicia el ciclo while
# Entonces volveriamos a sacar el ultimo digito y ya en el numero invertido como ya teniamos el ultimo digito guardado lo multiplicamos por 10 y le sumamos el digito que recien acabamos de sacar
# Y asi hasta que de 0 y se acabe el ciclo while

print(f"El numero invertido es: {num_invertido}")