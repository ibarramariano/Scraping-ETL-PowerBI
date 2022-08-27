# Paso 1: importo las librerías que voy a usar

from bs4 import BeautifulSoup
import requests

""" Paso 2: creo 2 variables, una para la URL y otra 
    que va a ser la ruta para el archivo de salida """

url = "https://subslikescript.com/movie/Titanic-120338"
ruta = 'Beautifulsoup&Request'

""" Paso 3: realizamos un requests para extraer los datos posteriormente,
    la extracción lo hacemos mediante una función """

def extracion_datos(url):

    try:
        results = requests.get(url)
    except Exception as e:
        print(f"Error de conexión!, código error:{e.message}")
    
    if results.status_code == 200:
        print("Conexión exitosa!")
        content = results.text
        return content

contenido = extracion_datos(url)

# BeautifulSoup nos permite organizar el HTML y darle formato para ser usado con python
 
soup = BeautifulSoup(contenido, 'html.parser')

# Extraemos el título

titulo = soup.find("h1").get_text()

""" Extraemos la transcipción, podemos extraer el contenido que querramos del HTML,
    para eso previamente tenemos que saber que etiqueda deseamos, una manera es 
    inspeccionando el contenido de la web en el navegador """

transcripcion = soup.find("div", class_="full-script").get_text(strip=True,separator=" ")

# Visualizamos por consola el resultado de la extración

print(titulo)
print(transcripcion)

# Paso 4: guardamos el resultado en un archivo txt

with open(f"{ruta}\{titulo}.txt", "w", encoding='utf-8') as file:
    file.write(titulo + "\n")
    file.write(transcripcion)

file.close()