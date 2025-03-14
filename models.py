from logger import color_text, Color


class Character:
    def __init__(self, username, password):
        self._username = username
        self._password = password

        self.hp = None
        self.max_hp = None
        self.mp = None
        self.max_mp = None

        self.is_exists_trauma = False

    def __str__(self):
        hp_str = color_text(f'HP: {self.hp}/{self.max_hp}', Color.RED)
        mp_str = color_text(f'MP: {self.mp}/{self.max_mp}', Color.BLUE)
        trauma_str = color_text("(+)" if self.is_exists_trauma else "", Color.YELLOW)
        message = f'<{color_text(self._username, Color.CYAN)}> ({hp_str}, {mp_str}) {trauma_str}'

        return message

    def is_healthy(self):
        return not self.is_exists_trauma and (self.hp / self.max_hp) > 0.9
