from faker import Faker

fake = Faker()


class BalanceData:
    def __init__(
        self,
        name: str = None,
        card_number: str = None,
        date_card: str = None,
        money: str = None,
    ):
        self.name = name
        self.card_number = card_number
        self.date_card = date_card
        self.money = money

    @staticmethod
    def random():
        name = fake.name()
        card_number = "1" * 16
        date_card = "12/29"
        money = "1000"
        return BalanceData(
            name=name, card_number=card_number, date_card=date_card, money=money
        )
