from russian_system import (
    Mir,
    VTB
)
from american_system import MasterCard
from adapter import Adapter


def client_code():
    onwer_1 = Mir(500)
    onwer_2 = MasterCard(600)
    onwer_3 = VTB(1000)

    adapter = Adapter(onwer_1,onwer_2)
    adapter.translation_into_russian(300)

    adapter2 = Adapter(onwer_3,onwer_2)
    adapter2.translation_into_american(200)

client_code()