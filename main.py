from dotenv import load_dotenv
import utils.execute_browser
import os

# from requests import auth
from utils.bearer_auth import BearerAuth
# from bs4 import BeautifulSoup

load_dotenv()

if __name__ == "__main__":
    grafana_ip = os.getenv("GRAFANA_IP", "192.168.1.69")
    grafana_port = os.getenv("GRAFANA_PORT", "3000")
    grafana_token = os.getenv("GRAFANA_TOKEN", "")

    url = f"http://{grafana_ip}:{grafana_port}"
    result = utils.execute_browser.take_screenshot(url)
    print(result)
