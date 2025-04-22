import requests
from bs4 import BeautifulSoup
import warnings
from urllib3.exceptions import InsecureRequestWarning

warnings.filterwarnings("ignore", category=InsecureRequestWarning)

url = "https://www.ideam.gov.co/"

try:
    response = requests.get(url, verify=False)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        titles = soup.find_all('h3')

        for title in titles:
            print(title.get_text())
    else:
        print(f"Error al acceder al sitio. Código de estado: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Ocurrió un error: {e}")
