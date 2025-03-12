import time
from urllib.parse import urlparse, parse_qs

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from actions import find_battle, go_to_forest
from auth import login
from constants import SMALL_RANDOM, BIG_RANDOM, MIDDLE_RANDOM
from pages import start
from utils import get_url


def main():
    d = webdriver.Chrome()

    start(d)
    char = login(d)

    while True:
        find_battle(d, char)

        if get_url(d).path == '/wap/main.php':
            my_char_link = d.find_element(By.XPATH, "//a[contains(@href, 'game.php')]")
            my_char_link.click()

            time.sleep(SMALL_RANDOM)

        if get_url(d).path == '/wap/game.php':
            char.update_info(d)

            if not char.is_healthy():
                time.sleep(BIG_RANDOM)
            else:
                try:
                    city = d.find_element(By.XPATH, "//a[contains(@href, 'gorod.php')]")
                    city.click()
                    time.sleep(SMALL_RANDOM)

                    wild_link = d.find_element(By.XPATH, "//a[contains(@href, 'teritory.php')]")
                    wild_link.click()
                    time.sleep(SMALL_RANDOM)
                except NoSuchElementException:
                    current_site = d.find_element(By.XPATH, "//a[contains(@href, 'teritory.php')]")
                    current_site.click()
                    time.sleep(SMALL_RANDOM)
                finally:
                    go_to_forest(d, char)

        if get_url(d).path == '/wap/gorod.php' and char.is_healthy():
            wild_link = d.find_element(By.XPATH, "//a[contains(@href, 'teritory.php')]")
            wild_link.click()
            time.sleep(SMALL_RANDOM)

            go_to_forest(d, char)

        d.refresh()
        time.sleep(MIDDLE_RANDOM)

    # driver.quit()


if __name__ == '__main__':
    main()
