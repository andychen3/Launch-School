# https://launchschool.com/exercises/cc086a2c

class Wallet:

    def __init__(self, amount):
        self.amount = amount

    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, amount):
        self._amount = amount

    def __add__(self, other):
        if not isinstance(other, Wallet):
            return NotImplemented
        
        new_amount = self.amount + other.amount
        return Wallet(new_amount)

wallet1 = Wallet(50)
wallet2 = Wallet(30)
merged_wallet = wallet1 + wallet2
print(merged_wallet.amount == 80)       # True
        
