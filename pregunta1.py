import requests

def obtener_precio_bitcoin():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status() 

        data = response.json()
        precio_usd = data['bpi']['USD']['rate_float']

        return precio_usd
    except requests.RequestException as e:
        print(f"Error al obtener el precio de Bitcoin: {e}")
        return None

def main():
    try:
        cantidad_bitcoins = float(input("Ingrese la cantidad de Bitcoins que posee: "))
    except ValueError:
        print("Por favor, ingrese un valor valido.")
        return


    precio_actual = obtener_precio_bitcoin()

    if precio_actual is not None:
        costo_en_usd = cantidad_bitcoins * precio_actual

        print(f"El costo actual de {cantidad_bitcoins} Bitcoins es: ${costo_en_usd:,.4f}")

if __name__ == "__main__":
    main()
