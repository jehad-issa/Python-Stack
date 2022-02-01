from BankAccount import BankAccount
class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = BankAccount
    def make_deposit(self, amount):
        self.account_balance.deposit(amount)
        return self
    def make_withdrawal(self, amount):
        self.account_balance.withdraw(amount)
        return self
    def display_user_balance(self):
        print(self.account_balance.display_account_info)


# jehad = User("jehad","jehadissa93@gmail.com")
# guido = User("Guido van Rossum", "guido@python.com")
# monty = User("Monty Python", "monty@python.com")  
# # Have the first user make 3 deposits and 1 withdrawal and then display their balance
# jehad.make_deposit(200)
# jehad.make_deposit(400)
# jehad.make_deposit(50)
# jehad.make_withdrawal(160)
# print(jehad.account_balance)
# jehad.display_user_balance()
# # Have the second user make 2 deposits and 2 withdrawals and then display their balance
# guido.make_deposit(300)
# guido.make_deposit(500)
# guido.make_withdrawal(160)
# guido.make_withdrawal(100)
# print(guido.account_balance)
# guido.display_user_balance()
# # Have the third user make 1 deposits and 3 withdrawals and then display their balance
# monty.make_deposit(600)
# monty.make_withdrawal(160)
# monty.make_withdrawal(80)
# monty.make_withdrawal(200)
# print(monty.account_balance)
# monty.display_user_balance()