def contar_lineas_codigo(archivo):
    try:
        if archivo.endswith(".py"):
            with open(archivo, 'r') as file:
                lineas = file.readlines()
                lineas_codigo = 0

                for linea in lineas:
                    linea_limpia = linea.strip()
                    if linea_limpia and not linea_limpia.startswith("#"):
                        lineas_codigo += 1

                return lineas_codigo
        else:
            print("El archivo debe tener extensión .py")
            return 0
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return 0

ruta_archivo = input("Ingrese la ruta del archivo .py: ")
cantidad_lineas = contar_lineas_codigo(ruta_archivo)

if cantidad_lineas > 0:
    print(f"El archivo {ruta_archivo} tiene {cantidad_lineas} líneas de código.")
