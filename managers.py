import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from constants import MIDDLE_RANDOM
from gateways import DriverGateway
from models import Character
from logger import log




class CharacterManager:
    def __init__(self, character: Character, driver_gw: DriverGateway):
        self.character = character
        self.driver_gw = driver_gw

    def update_character_info(self):
        log.debug('Обновляю параметры персонажа.')

        self.driver_gw.refresh()

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

        log.info(str(self.character))

    def find_battle(self):
        log.debug('Поиск битвы...')
        if self.driver_gw.check_url_path('/wap/boj.php'):
            log.warning('Персонаж в бою! 😱')
            try:
                while True:
                    self.driver_gw.button_click('bitvraga')
                    log.info('Удар!')

            except NoSuchElementException:
                log.info('Бой окончен.')

                if self.driver_gw.check_url_path('/wap/wait.php'):
                    log.debug('Информация о результатах боя еще недоступна, подождем...')
                    self.driver_gw.refresh()
                    time.sleep(MIDDLE_RANDOM)

                if self.driver_gw.check_url_path('/wap/logfull.php'):
                    log.debug('Результаты боя готовы. Перейдем на страницу персонажа для обновления характеристик.')
                    self.driver_gw.link_click_by_href('game.php')
                    self.update_character_info()

                    if not self.character.is_healthy():
                        log.info('Персонаж потерял слишком много здоровья, возвращаемся в город.')
                        self.driver_gw.link_click_by_href('teleport.php')

    def to_game_page(self):
        log.info('Перемещаемся на страницу с информацией о персонаже.')
        self.driver_gw.link_click_by_href('game.php')
        self.find_battle()

    def check_main_page(self):
        if self.driver_gw.check_url_path('/wap/main.php'):
            self.to_game_page()

    def check_game_page(self):
        if self.driver_gw.check_url_path('/wap/game.php'):
            self.update_character_info()

            while not self.character.is_healthy():
                if self.character.is_exists_trauma:
                    log.info('Персонаж получил травму, идем лечиться.')
                    self.driver_gw.link_click_by_href('main.php')
                    self.driver_gw.link_click_by_href('gorod.php')
                    self.driver_gw.link_click_by_href('arena.php')
                    self.driver_gw.link_click_by_href('arena_travma.php')
                    self.driver_gw.link_click_by_href('main.php')
                    self.driver_gw.link_click_by_href('game.php')
                    log.info('Лечение прошло успешно.')

                time.sleep(MIDDLE_RANDOM)
                self.update_character_info()
            else:
                self.driver_gw.link_click_by_href('main.php')

                self.find_battle()

                try:
                    self.driver_gw.link_click_by_href('gorod.php')
                    self.driver_gw.link_click_by_href('teritory.php')
                except NoSuchElementException:
                    self.driver_gw.link_click_by_href('teritory.php')
                finally:
                    log.info('Выходим на природу.')
                    self.find_battle()

                    if self.driver_gw.get_current_square_id() == 'r394':
                        self.go_to_forest()

    def check_city_page(self):
        if self.driver_gw.check_url_path('/wap/gorod.php'):
            if self.character.is_healthy():
                log.info('Выходим на природу.')
                self.driver_gw.link_click_by_href('teritory.php')

                if self.driver_gw.get_current_square_id() == 'r394':
                    self.go_to_forest()
            else:
                self.to_game_page()

    def go_to_forest(self):
        self.find_battle()
        log.info('Шагаем на клетку r395.')
        self.driver_gw.link_click_by_id('r395')
        log.info('Шагаем на клетку r431.')
        self.driver_gw.link_click_by_id('r431')
        log.info('Шагаем на клетку r467.')
        self.driver_gw.link_click_by_id('r467')
        log.info('Шагаем на клетку r503.')
        self.driver_gw.link_click_by_id('r503')
        log.info('Шагаем на клетку r504.')
        self.driver_gw.link_click_by_id('r504')
        log.info('Шагаем на клетку r470.')
        self.driver_gw.link_click_by_id('r470')
