class Money:

    def __init__(self, amount_of_currency, relevance):
        self.amount_of_currency = amount_of_currency
        self.relevance = relevance

    def change_amount_of_money(self, new_amount):
        self.amount_of_currency = new_amount

    def ban_on_use(self, resolution=True):
        self.ban = resolution

class Cash(Money):

    def __init__(self, type_of_currency, ratio_to_GBT, amount_of_currency, relevance):
        super().__init__(amount_of_currency, relevance)
        self.type_of_currency = type_of_currency
        self.ratio_to_GBT = ratio_to_GBT
        self.material = material

    def should_invest(self, resolution=True):
        self.should_invest = resolution

class NonCashMoney(Money):

   	def __init__(self, bank='Sber', amount_of_currency, relevance):
        super().__init__(amount_of_currency, relevance)
        self.bank = bank

    def transfer(self, bank):
        self.bank = bank


class Wallet:

    def __init__(self, money):
        self.money = money

    def pay(self, amount):
        money.amount_of_currency -= amount
        return f'Из кошелька было взято денег на сумму {amount}'

    def put_money(self, amount)
        money.amount_of_currency += amount
        return f'Кошелёк пополнен на сумму {amount}'


class CashWallet(Wallet):

    def __init__(self, money, discont_cards):
        super().__init__(money)
        self.discont_cards = discont_cards

    def add_discont_cards(discont_card):
        self.discont_cards.append(discont_card)
        return f'У вас новая дисконтная карта: {discont_cards}!'


class NonCashWallet(Wallet):

    def send_email(self, amount)
        return f'Ваш чек по операции на сумму {amount}'

    def pay(self, amount):
        money.amount_of_currency -= amount
        self.send_email(amount)
        return f'Из кошелька было взято денег на сумму {amount}'

    def put_money(self, amount)
        money.amount_of_currency += amount
        self.send_email(amount)
        return f'Кошелёк пополнен на сумму {amount}'
