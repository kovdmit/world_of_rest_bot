import time

from auth import login
from constants import MIDDLE_RANDOM
from drivers import get_chrome_driver
from gateways import DriverGateway
from managers import CharacterManager


def main():
    driver_gw = DriverGateway(get_chrome_driver())
    driver_gw.start()
    manager = CharacterManager(login(driver_gw), driver_gw)

    while True:
        try:
            manager.find_battle()
            manager.check_main_page()
            manager.check_game_page()
            manager.check_city_page()

            driver_gw.refresh()
            time.sleep(MIDDLE_RANDOM)

        except Exception:
            pass


if __name__ == '__main__':
    main()
