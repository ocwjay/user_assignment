#Defining user class
class user():
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(f'User: {self.name}, ${self.account_balance}')
    def transfer_money(self, otherUser, amount):
        self.account_balance -= amount
        otherUser.account_balance += amount
        print(f'User: {self.name}, ${self.account_balance}')
        print(f'User: {otherUser.name}, ${otherUser.account_balance}')

#Making users
robert = user('Robert', 'robert@someaddress.com')
eric = user('Eric', 'eric@someaddress.com')
jay = user('Jay', 'jay@someaddress.com')

#the first user makes 3 deposits and one withdrawal. then we display their balance
robert.make_deposit(320)
robert.make_deposit(150)
robert.make_deposit(804)
robert.make_withdrawal(600)
robert.display_user_balance()
#the second user makes 2 deposits and 2 withdrawals. then we display their balance
eric.make_deposit(2400)
eric.make_deposit(780)
eric.make_withdrawal(48)
eric.make_withdrawal(206)
eric.display_user_balance()
#the third user makes 1 deposit and 3 withdrawals. then we display their balance
jay.make_deposit(964)
jay.make_withdrawal(94)
jay.make_withdrawal(200)
jay.make_withdrawal(63)
jay.display_user_balance()

#BONUS: create transfer method. Have the first user transfer money to the second user, and display both users' balances
robert.transfer_money(jay, 52)