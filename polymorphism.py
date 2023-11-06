class Money:

    def __init__(self, amount_of_currency, relevance):
        self.amount_of_currency = amount_of_currency
        self.relevance = relevance

    def change_amount_of_money(self, new_amount):
        self.amount_of_currency = new_amount

    def ban_on_use(self, resolution=True):
        self.ban = resolution

    def is_enough(self):
        return 'YES' if self.amount_of_currency >= 100 else 'NO'

class Cash(Money):

    def __init__(self, type_of_currency, ratio_to_GBT, amount_of_currency, relevance):
        super().__init__(amount_of_currency, relevance)
        self.type_of_currency = type_of_currency
        self.ratio_to_GBT = ratio_to_GBT
        self.material = material

    def should_invest(self, resolution=True):
        self.should_invest = resolution

    def is_enough(self):
        return 'YES' if self.amount_of_currency >= 150 else 'NO'

class NonCashMoney(Money):

    def __init__(self, bank='Sber'):
        super().__init__(amount_of_currency, relevance)
        self.bank = bank

    def transfer(self, bank):
        self.bank = bank

    def is_enough(self):
        return 'YES' if self.amount_of_currency >= 120 else 'NO'

class Wallet:

    def __init__(self, money):
        self.money = money

    def pay(self, amount):
        money.amount_of_currency -= amount
        return f'Из кошелька было взято денег на сумму {amount}'

    def put_money(self, amount):
        money.amount_of_currency += amount
        return f'Кошелёк пополнен на сумму {amount}'


class CashWallet(Wallet):

    def __init__(self, money = 10, discont_cards = ''):
        super().__init__(money)
        self.discont_cards = discont_cards

    def add_discont_cards(self, discont_card):
        return f'У вас новая дисконтная карта: {discont_card}' \
               f'!'


class NonCashWallet(Wallet):

    def send_email(self, amount):
        return f'Ваш чек по операции на сумму {amount}'

    def pay(self, amount):
        self.money -= amount
        self.send_email(amount)
        return f'Из кошелька было взято денег на сумму {amount}'

    def put_money(self, amount):
        self.money += amount
        self.send_email(amount)
        return f'Кошелёк пополнен на сумму {amount}'

class CryptoWallet(NonCashWallet, CashWallet):
    pass

crypto_wallet_1 = CryptoWallet()
crypto_wallet_1.put_money(100)
crypto_wallet_1.add_discont_cards('Monetka')

class FooBar:
    pass


class Foo(FooBar):
    def _init_(self, name):
        self.name = name

    def print_phrase(self):
        return 'Foo'


class Bar(FooBar):
    def _init_(self, name):
        self.name = name

    def print_phrase(self):
        return 'Bar'

foo = [Foo(f"Foo_{i}") for i in range(250)]
bar = [Bar(f"Bar_{i}") for i in range(250)]
foo_bar = foo + bar

for i in range(500):
    print(foo_bar[i].print_phrase())
