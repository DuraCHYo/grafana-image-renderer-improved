from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import datetime
import os

options = Options()
# options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--window-size=1920,1080")

service = Service(
    "/Users/depishev/Documents/PycharmProjects/grafana-image-renderer-improved/chromedriver-mac-arm64/chromedriver"
)


# def interceptor(request):
#    request.headers["Authorization"] = f"Basic {os.getenv('GRAFANA_TOKEN')}"


def take_screenshot(url, filename=None):
    driver = webdriver.Chrome(service=service, options=options)
    #    driver.request_interceptor = interceptor
    try:
        driver.get(url)
        time.sleep(1)

        if filename is None:
            current_timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{current_timestamp}.png"

        driver.save_screenshot(filename)
        return filename
    except Exception as e:
        print(f"Ошибка: {e}")
        return None

    finally:
        driver.quit()
