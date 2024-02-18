import requests

def obtener_precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  
        data = response.json()
        precio_bitcoin = data["bpi"]["USD"]["rate"]
        return precio_bitcoin
    except requests.RequestException as e:
        print(f"Error al obtener el precio de Bitcoin: {e}")
        return None

def almacenar_precio_en_archivo(precio, archivo):
    try:
        with open(archivo, "a") as file:
            file.write(f"{precio}\n")
        print(f"Datos almacenados en {archivo}")
    except IOError as e:
        print(f"Error al escribir en el archivo: {e}")


precio_actual = obtener_precio_bitcoin()

if precio_actual is not None:
    archivo_txt = "precios_bitcoin.txt"
    almacenar_precio_en_archivo(precio_actual, archivo_txt)
