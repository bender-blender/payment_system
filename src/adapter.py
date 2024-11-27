from interface import IPaymentSystem
from pay_systems import PayPal


class AdapterPal(IPaymentSystem):
    """Адаптер для PayPal

    Args:
        IPaymentSystem (_type_): _description_
    """
    def __init__(self,system:PayPal):
        self.system = system

    def pay(self, amount: int, number: str):
        if number.startswith("555"):
            self.system.pay_pal(amount,number)
        else:
            print("Не работаем")
