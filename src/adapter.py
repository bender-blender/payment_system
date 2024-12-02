from interface import (
    AmericanSystem,
    RussianSystem
)


class Adapter:
    """Адапетр
    """

    def __init__(self,russian:RussianSystem,american:AmericanSystem):
        self.ru = russian
        self.us = american
    
    def translation_into_russian(self,value:int):
        """Перевод через адаптер на русскую систему
        """
        self.ru.code = "us"
        self.us.shifting(self.ru,value)
        self.ru.code = "ru"
    
    def translation_into_american(self,value:int):
        """Перевод через адаптер на американскую систему
        """
        self.us.code = "ru"
        self.ru.translation(self.us,value)
        self.us.code = "us"


        

