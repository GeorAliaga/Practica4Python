import requests
from io import BytesIO
import zipfile
from PIL import Image

url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

response = requests.get(url)
image_bytes = BytesIO(response.content)


with open("imagen.jpg", "wb") as image_file:
    image_file.write(image_bytes.getvalue())



with zipfile.ZipFile("imagenes.zip", "w") as zip_file:
    zip_file.write("imagen.jpg")

with zipfile.ZipFile("imagenes.zip", "r") as zip_file:
    zip_file.extractall("descomprimido")




imagen_descomprimida_path = "descomprimido/imagen.jpg"
Image.open(imagen_descomprimida_path).show()
