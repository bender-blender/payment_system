from interface import RussianSystem

import time


class Mir(RussianSystem):
    """Система Мир

    Args:
        RussianSystem (_type_): _description_
    """

    def __init__(self, check):
        self.name = "Мир"
        self.code = "ru"
        self.check = check
        

class VTB(RussianSystem):
    """ВТБ

    Args:
        RussianSystem (_type_): _description_
    """
    def __init__(self, check):
        self.name = "ВТБ"
        self.check = check
        self.code = "ru"