from abc import ABC,abstractmethod

class IPaymentSystem(ABC):
    """Система оплаты

    Args:
        ABC (_type_): _description_
    """
    @abstractmethod
    def pay(self, amount:int, number:str): 
        """
        Оплата
        Args:
            amount (_type_):Сумма
            account (_type_):Номер карты

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError
