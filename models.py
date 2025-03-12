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
        return f'<Character {self._username}> (HP: {self.hp}/{self.max_hp}, MP: {self.mp}/{self.max_mp}) {"+" if self.is_exists_trauma else ""}'

    def is_healthy(self):
        return not self.is_exists_trauma and (self.hp / self.max_hp) > 0.9
