
class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	
        self.account_balance += amount	
        return self
    # adding the make_withdrawal method
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    # Add a display_user_balance
    def display_user_balance(self):
        print("name :",self.name,"account_balance :" ,self.account_balance)

jehad = User("jehad","jehadissa93@gmail.com")
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")  
# Have the first user make 3 deposits and 1 withdrawal and then display their balance
# jehad.make_deposit(200)
# jehad.make_deposit(400)
# jehad.make_deposit(50)
# jehad.make_withdrawal(160)
# print(jehad.account_balance)
# jehad.display_user_balance()
jehad.make_deposit(200).make_deposit(400).make_deposit(50).make_withdrawal(160).display_user_balance()
# Have the second user make 2 deposits and 2 withdrawals and then display their balance
# guido.make_deposit(300)
# guido.make_deposit(500)
# guido.make_withdrawal(160)
# guido.make_withdrawal(100)
# print(guido.account_balance)
# guido.display_user_balance()
guido.make_deposit(300).make_deposit(500).make_withdrawal(160).make_withdrawal(100).display_user_balance()
# Have the third user make 1 deposits and 3 withdrawals and then display their balance
# monty.make_deposit(600)
# monty.make_withdrawal(160)
# monty.make_withdrawal(80)
# monty.make_withdrawal(200)
# print(monty.account_balance)
# monty.display_user_balance()
monty.make_deposit(600).make_withdrawal(160).make_withdrawal(80).make_withdrawal(200).display_user_balance()