from interface import IPaymentSystem

class OsadchiySystem(IPaymentSystem):
    """Система Осадчего

    Args:
        IPaymentSystem (_type_): _description_
    """
    
    def __init__(self,owner:str, check:int, number:str):
        self.owner = owner
        self.check = check
        self.number = "555" + number

    def pay(self, amount: int, number: str):
        
        print(f"Оплата прошла успешно по номеру:{number}")
        self.check -= amount

    def __str__(self) -> str:
        return f"Ф.И.О {self.owner}\nНомер {self.number}\nБаланс:{self.check}"
    


class PayPal:
    """Пай Пел
    """
    def __init__(self,owner:str, check:int, number:str):
        self.owner = owner
        self.check = check
        self.number = "555" + number

    def pay_pal(self, amount: int, number: str):
        if number.startswith("555"):
            print(f"Оплата прошла успешно по номеру:{number}")
            self.check -= amount
        else:
            print("С такой системой не работаем")
    
    def __str__(self) -> str:
        return f"Ф.И.О {self.owner}\nНомер {self.number}\nБаланс:{self.check}"