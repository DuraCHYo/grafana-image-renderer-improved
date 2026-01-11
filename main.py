from dotenv import load_dotenv
import os
import requests

# from requests import auth
from utils.bearer_auth import BearerAuth
# from bs4 import BeautifulSoup

load_dotenv()

url = f"http://192.168.1.69:{os.getenv('GRAFANA_PORT')}"
# headers = {"Authorization": f"Bearer {os.getenv('GRAFANA_TOKEN')}"}

r = requests.get(url=url, auth=BearerAuth(os.getenv("GRAFANA_TOKEN")))
print(r)
