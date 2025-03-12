import time

from selenium.webdriver.common.by import By

from config import PASSWORD, USERNAME
from constants import MIDDLE_RANDOM
from models import Character


def login(driver):
    char = Character(USERNAME, PASSWORD)

    login_input = driver.find_element(By.NAME, 'pname')
    password_input = driver.find_element(By.NAME, 'pass')

    login_input.send_keys(char._username)
    password_input.send_keys(char._password)

    login_button = driver.find_element(By.NAME, 'login')
    login_button.click()

    time.sleep(MIDDLE_RANDOM)

    return char
