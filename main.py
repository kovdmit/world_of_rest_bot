import time

from selenium import webdriver

from auth import login
from constants import MIDDLE_RANDOM
from gateways import DriverGateway
from managers import CharacterManager


def main():
    driver_gw = DriverGateway(webdriver.Chrome())
    driver_gw.start()
    manager = CharacterManager(login(driver_gw), driver_gw)

    while True:
        manager.find_battle()
        manager.check_main_page()
        manager.check_game_page()
        manager.check_city_page()

        driver_gw.refresh()
        time.sleep(MIDDLE_RANDOM)


if __name__ == '__main__':
    main()
