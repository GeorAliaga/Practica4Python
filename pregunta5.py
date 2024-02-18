def guardar_tabla_multiplicar(numero):
    try:
        with open(f'tabla-{numero}.txt', 'w') as file:
            for i in range(1, 11):
                resultado = numero * i
                file.write(f"{numero} x {i} = {resultado}\n")
        print(f"Tabla de multiplicar para {numero} guardada en tabla-{numero}.txt")
    except IOError as e:
        print(f"Error al escribir en el archivo: {e}")

def mostrar_tabla_multiplicar(numero):
    try:
        with open(f'tabla-{numero}.txt', 'r') as file:
            contenido = file.read()
            print(f"Tabla de multiplicar para {numero}:\n{contenido}")
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")

def mostrar_linea_tabla_multiplicar(numero, linea):
    try:
        with open(f'tabla-{numero}.txt', 'r') as file:
            lineas = file.readlines()
            if 1 <= linea <= len(lineas):
                print(f"Linea {linea}: {lineas[linea - 1]}")
            else:
                print(f"Linea {linea} no valida para la tabla de multiplicar de {numero}.")
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")

while True:
    print("1. Guardar tabla de multiplicar")
    print("2. Mostrar tabla de multiplicar")
    print("3. Mostrar linea de tabla de multiplicar")
    print("4. Salir")

    opcion = input("Seleccione una opcion (1-4): ")

    if opcion == "1":
        numero = int(input("Ingrese un numero entre 1 y 10: "))
        if 1 <= numero <= 10:
            guardar_tabla_multiplicar(numero)
        else:
            print("Numero fuera de rango. Debe estar entre 1 y 10.")
    elif opcion == "2":
        numero = int(input("Ingrese un numero entre 1 y 10: "))
        if 1 <= numero <= 10:
            mostrar_tabla_multiplicar(numero)
        else:
            print("Número fuera de rango. Escriba numero entre 1 y 10.")
    elif opcion == "3":
        numero = int(input("Ingrese un numero entre 1 y 10: "))
        linea = int(input("Ingrese el numero de linea a mostrar: "))
        if 1 <= numero <= 10:
            mostrar_linea_tabla_multiplicar(numero, linea)
        else:
            print("Numero fuera de rango. Escriba numero entre 1 y 10.")
    elif opcion == "4":
        print("¡Adiós!")
        break
    else:
        print("Opcion no valida. Intentelo de nuevo.")
