class BankAccount:
  def __init__(self, account_num, balance):
    self.__account_num = account_num
    if balance >= 0:
        self.__balance = balance
    else: 
        self.__balance = 0
  def gt_account_number(self):
    return self.__account_num
  def gt_balance(self):
    return self.__balance

  def withdraw(self, amount): 
    if amount <= 0:
        print("Withdrawal amount must be positive.")
    elif amount > self.__balance:
        print("Insufficient funds.")
    else: 
        self.__balance -= amount 
        print("Withdrawal successful.")
  def deposit(self, amount):
    if amount > 0:
        self.__balance += amount
        print("Deposit successful!")
    else: 
        print("Deposit amount should be postive")


account1 = BankAccount("87654321", 9876)

print(account1.gt_account_number())
print(account1.gt_balance())

account1.deposit(222)
account1.withdraw(1000)

print(account1.gt_balance())
