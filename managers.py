import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from constants import MIDDLE_RANDOM, BIG_RANDOM
from gateways import DriverGateway
from models import Character


class CharacterManager:
    def __init__(self, character: Character, driver_gw: DriverGateway):
        self.character = character
        self.driver_gw = driver_gw

    def update_character_info(self):
        hp_span = self.driver_gw.find_element(By.XPATH, "//img[@src='img/hp.png']/following::*[2]")
        mp_span = self.driver_gw.find_element(By.XPATH, "//img[@src='img/ma.png']/following::*[2]")
        trauma_img = self.driver_gw.find_element(By.XPATH, "//img[@src='img/aid.gif']")
        trauma = self.driver_gw.execute_script(
            "return arguments[0].nextSibling.textContent;",
            trauma_img
        ).strip()

        self.character.hp = int(hp_span.text.split('/')[0])
        self.character.max_hp = int(hp_span.text.split('/')[1])
        self.character.mp = int(mp_span.text.split('/')[0])
        self.character.max_mp = int(mp_span.text.split('/')[1])
        self.character.is_exists_trauma = True if trauma != 'Нет' else False

        print(self.character)

    def find_battle(self):
        if self.driver_gw.check_url_path('/wap/boj.php'):
            try:
                while True:
                    self.driver_gw.button_click('bitvraga')

            except NoSuchElementException:
                if self.driver_gw.check_url_path('/wap/wait.php'):
                    self.driver_gw.refresh()
                    time.sleep(MIDDLE_RANDOM)

                if self.driver_gw.check_url_path('/wap/logfull.php'):
                    self.driver_gw.link_click_by_href('game.php')
                    self.update_character_info()

                    if not self.character.is_healthy():
                        self.driver_gw.link_click_by_href('teleport.php')

    def to_game_page(self):
        self.driver_gw.link_click_by_href('game.php')
        self.find_battle()

    def check_main_page(self):
        if self.driver_gw.check_url_path('/wap/main.php'):
            self.to_game_page()

    def check_game_page(self):
        if self.driver_gw.check_url_path('/wap/game.php'):
            self.update_character_info()

            if not self.character.is_healthy():
                if self.character.is_exists_trauma:
                    self.driver_gw.link_click_by_href('main.php')
                    self.driver_gw.link_click_by_href('gorod.php')
                    self.driver_gw.link_click_by_href('arena.php')
                    self.driver_gw.link_click_by_href('arena_travma.php')
                    self.driver_gw.link_click_by_href('main.php')

                time.sleep(BIG_RANDOM)
            else:
                self.driver_gw.link_click_by_href('main.php')

                self.find_battle()

                try:
                    self.driver_gw.link_click_by_href('gorod.php')
                    self.driver_gw.link_click_by_href('teritory.php')
                except NoSuchElementException:
                    self.driver_gw.link_click_by_href('teritory.php')
                finally:
                    self.find_battle()

                    if self.driver_gw.get_current_square_id() != 'r470':
                        self.go_to_forest()

    def check_city_page(self):
        if self.driver_gw.check_url_path('/wap/gorod.php'):
            if self.character.is_healthy():
                self.driver_gw.link_click_by_href('teritory.php')

                if self.driver_gw.get_current_square_id() != 'r470':
                    self.go_to_forest()
            else:
                self.to_game_page()

    def go_to_forest(self):
        self.find_battle()
        self.driver_gw.link_click_by_id('r395')
        self.driver_gw.link_click_by_id('r431')
        self.driver_gw.link_click_by_id('r467')
        self.driver_gw.link_click_by_id('r503')
        self.driver_gw.link_click_by_id('r504')
        self.driver_gw.link_click_by_id('r470')
