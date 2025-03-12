from selenium.webdriver.common.by import By


class Character:
    def __init__(self, username, password):
        self._username = username
        self._password = password

        self.hp = None
        self.max_hp = None
        self.mp = None
        self.max_mp = None

        self.is_exists_trauma = False

    def update_info(self, d):
        hp_span = d.find_element(By.XPATH, "//img[@src='img/hp.png']/following::*[2]")
        mp_span = d.find_element(By.XPATH, "//img[@src='img/ma.png']/following::*[2]")
        trauma_img = d.find_element(By.XPATH, "//img[@src='img/aid.gif']")
        trauma = d.execute_script(
            "return arguments[0].nextSibling.textContent;",
            trauma_img
        ).strip()

        self.hp = int(hp_span.text.split('/')[0])
        self.max_hp = int(hp_span.text.split('/')[1])
        self.mp = int(mp_span.text.split('/')[0])
        self.max_mp = int(mp_span.text.split('/')[1])
        self.is_exists_trauma = True if trauma != 'Нет' else False

    def is_healthy(self):
        return not self.is_exists_trauma and (self.hp / self.max_mp) > 0.5