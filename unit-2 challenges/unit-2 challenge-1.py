def _init_(self, account_number, account_holder_name, initial_balance=0.0):
  self.__account_number = account_number
  self.__account_holder_name = account_holder_name
  self.__account_balance = initial_balance

def deposit(self, amount):
  if amount > 0:
      self.__account_balance += amount
      return f"Deposited ${amount}. New balance: ${self.__account_balance}"
  else:
      return "Invalid deposit amount."

def withdraw(self, amount):
  if 0 < amount <= self.__account_balance:
      self.__account_balance -= amount
      return f"Withdrew ${amount}. New balance: ${self.__account_balance}"
  else:
      return "Invalid withdrawal amount or insufficient funds."

def display_balance(self):
  return f"Account Balance for {self._account_holder_name} (Account #{self.account_number}): ${self._account_balance}"

# Example usage:
if _name_ == "_main_":
account = BankAccount("12345", "John Doe", 1000.0)

print(account.display_balance())
print(account.deposit(500.0))
print(account.withdraw(200.0))
print(account.withdraw(1500.0))