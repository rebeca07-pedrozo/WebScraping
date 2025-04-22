import requests
from bs4 import BeautifulSoup
import warnings
from urllib3.exceptions import InsecureRequestWarning

warnings.filterwarnings("ignore", category=InsecureRequestWarning)

url = "https://www.ideam.gov.co/"
api_url = "http://0.0.0.0:5000/guardar"


try:
    response = requests.get(url, verify=False)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        titles = soup.find_all('h3')

        titles_data = {"titles": []}

        for title in titles:
            titles_data["titles"].append(title.get_text())  

        api_response = requests.post(api_url, json=titles_data)
        print(f"Respuesta de la API: {api_response.json()}")

    else:
        print(f"Error al acceder al sitio. Código de estado: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Ocurrió un error: {e}")
