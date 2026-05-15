class BankAccount:
    def __init__(self, B):
        self.balance = B
    def debited(self, A):
        self.amount = A
        if self.amount > self.balance:
            print("You cannot debit more than balance!")
        elif self.balance == 0:
            print("Your have zero balance!")
        else:
            self.balance -= self.amount
            print(f"Balance:- {self.balance}")
        
    def credited(self, C):
        self.amount = C
        self.balance += self.amount
        print(f"Balance:- {self.balance}")


balance = float(input("Enter your bank balance:- "))
B1 = BankAccount(balance)
while True:
   x = input("Are you want to debit(y/n):- ")
   if x.lower() == 'y':
      amnt = float(input("Enter amount:- "))
      B1.debited(amnt)
      break
   elif x.lower() == 'n':
      print("Ok!Then get lost.")
      break
   else:
      print("Invalid choice!")

while True:
   m = input("Are you want to credit(y/n):- ")
   if m.lower() == 'y':
      amnt = float(input("Enter amount:- "))
      B1.credited(amnt)
      break
   elif m.lower() == 'n':
      print("Ok!Then get lost.")
      break
   else:
      print("Invalid choice!")