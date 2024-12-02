from interface import AmericanSystem

class MasterCard(AmericanSystem):
    """Система Master Card

    Args:
        AmericanSystem (_type_): _description_
    """
    def __init__(self, check):
        self.name = "Master Card"
        self.code = "us"
        self.check = check
    