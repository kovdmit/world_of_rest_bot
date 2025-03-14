import time
from urllib.parse import urlparse

from selenium.webdriver.common.by import By

from constants import SMALL_RANDOM


class DriverGateway:
    def __init__(self, driver):
        self.driver = driver

    def save_screenshot(self, name: str):
        return self.driver.save_screenshot(name)

    def find_element(self, *args):
        return self.driver.find_element(*args)

    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    def refresh(self):
        return self.driver.refresh()

    def start(self):
        self.driver.get('https://wor.com.ua/wap/')
        time.sleep(SMALL_RANDOM)

    def check_url_path(self, path: str):
        return self._get_url().path == path

    def _get_url(self):
        current_url = self.driver.current_url
        parsed_url = urlparse(current_url)

        return parsed_url

    def link_click_by_href(self, href: str):
        self.driver.find_element(By.XPATH, f"//a[starts-with(@href, '{href}')]").click()
        time.sleep(SMALL_RANDOM)

    def link_click_by_id(self, id: str):
        self.driver.find_element(By.ID, id).click()
        time.sleep(SMALL_RANDOM)

    def button_click(self, name: str):
        self.driver.find_element(By.NAME, name).click()
        time.sleep(SMALL_RANDOM)

    def get_current_square_id(self):
        current_coord = self.find_element(By.XPATH, '//tbody/tr[3]/td[3]')
        div_coord = current_coord.find_element(By.XPATH, './*')

        return div_coord.get_attribute('id')
