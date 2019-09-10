# wallet.py
class Wallet:
    def __init__(self):
        self.balance = 0

    def add_cash(self, x):
        self.balance += x

    def spend_cash(self, x):
        self.balance -= x

# test_wallet.py
import pytest

'''
Fixtures: They help us set up some helper code that should run before 
any tests are executed, and are perfect for setting up resources 
that are needed by the tests.
'''
@pytest.fixture
def my_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Wallet()

def test_default_initial_amount(my_wallet):
    assert my_wallet.balance == 0

def test_wallet_add_cash(my_wallet):
    my_wallet.add_cash(80)
    assert my_wallet.balance == 80

@pytest.mark.parametrize("earned,spent,expected", [
    (30, 10, 20),
    (20, 2, 18),
])

def test_transactions(my_wallet, earned, spent, expected):
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected