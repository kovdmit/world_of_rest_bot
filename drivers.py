from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from config import DEBUG


def get_chrome_driver():
    if not DEBUG:
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("start-maximized")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--remote-debugging-port=9222")
        options.add_argument("--disable-software-rasterizer")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-infobars")
        options.add_argument("--mute-audio")
        options.add_argument(
            "user-agent=Mozilla/5.0 (X11; Linux x86_64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/134.0.0.0 Safari/537.36"
        )

        caps = DesiredCapabilities().CHROME
        caps["goog:loggingPrefs"] = {"performance": "ALL"}
        driver = webdriver.Chrome(service=Service(), options=options)

        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    else:
        driver = webdriver.Chrome()

    return driver
