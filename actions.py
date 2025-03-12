import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from constants import SMALL_RANDOM, MIDDLE_RANDOM, BIG_RANDOM
from utils import get_url


def find_battle(d, char):
    if get_url(d).path == '/wap/boj.php':
        try:
            while True:
                d.find_element(By.TAG_NAME, "form")
                attack_button = d.find_element(By.NAME, "bitvraga")
                attack_button.click()
                time.sleep(SMALL_RANDOM)
        except NoSuchElementException:
            if get_url(d).path == '/wap/wait.php':
                d.refresh()
                time.sleep(MIDDLE_RANDOM)
            if get_url(d).path == '/wap/logfull.php':
                char.update_info(d)

                my_char_link = d.find_element(By.XPATH, "//a[contains(@href, 'game.php')]")
                my_char_link.click()
                time.sleep(SMALL_RANDOM)

                if not char.is_healthy():
                    teleport = d.find_element(By.XPATH, "//a[contains(@href, 'teleport.php')]")
                    teleport.click()
                    time.sleep(BIG_RANDOM)


def go_to_forest(d, char):
    find_battle(d, char)
    r395 = d.find_element(By.ID, 'r395')
    r395.click()
    time.sleep(SMALL_RANDOM)

    find_battle(d, char)
    r431 = d.find_element(By.ID, 'r431')
    r431.click()
    time.sleep(SMALL_RANDOM)

    find_battle(d, char)
    r467 = d.find_element(By.ID, 'r467')
    r467.click()
    time.sleep(SMALL_RANDOM)

    find_battle(d, char)
    r503 = d.find_element(By.ID, 'r503')
    r503.click()
    time.sleep(SMALL_RANDOM)

    find_battle(d, char)
    r504 = d.find_element(By.ID, 'r504')
    r504.click()
    time.sleep(SMALL_RANDOM)

    find_battle(d, char)
    r470 = d.find_element(By.ID, 'r470')
    r470.click()
    time.sleep(SMALL_RANDOM)
