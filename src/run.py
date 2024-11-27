from pay_systems import (
    OsadchiySystem,
    PayPal
    )

from adapter import AdapterPal



def client_code():
    owner_one = OsadchiySystem("Осадчий Максим Сергеевич",100000000,"55564432")
    print(owner_one)
    
    owner_one.pay(500,"5565432")
    print()
    onwer_two = PayPal("Осадчий Сергей Сергеевич",500,"5553456")
    print(onwer_two)
    
    adapter = AdapterPal(onwer_two)
    adapter.pay(20,"5552468")
    adapter.pay(300,"543223")
client_code()