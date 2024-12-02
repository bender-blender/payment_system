

class RussianSystem:
    """Русская система

    Args:
        IBank (_type_): _description_
    """
    def __init__(self,check):
        self.name = None
        self.check = check
        self.code = "ru"

    def __str__(self) -> str:
        return f"{self.name}\nСчет:{self.check}"
    
    
    def translation(self, card, value:int):
        """Перевод внутри русской системы
        """
        if card.code == "ru":
            self.check -= value
            card.check += value
            print(f"Перевод из системы {self.name} в {card.name} завершен")
        else:
            print("Переводы за границу ЗАПРЕЩЕНЫ!")


class AmericanSystem:
    """Американская система
    """
    def __init__(self,check):
        self.name = None 
        self.check = check
        self.code = "us"
    
    def __str__(self) -> str:
        return f"{self.name}\nСчет:{self.check}"

   
    def shifting(self, card, value:int):
        if card.code == "us":
            self.check -= value
            card.check += value
            print(f"Transfer from {self.name} to {card.name} completed")
        else:
            print("Transfers abroad are PROHIBITED!")



