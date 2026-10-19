class BankAccount:
  def __init__(self, account_num, balance):
    self.__account_num = account_num
    self.__balance = balance

  def set_account_num(self, account_num):
    self.__account_num = account_num

  def set_balance(self, balance):
    if balance >= 0: 
       self.__balance = balance
    else:
      print("Balance cannot be negative.")

  def gt_account_num(self):
    return self.__account_num

  def gt_balance(self):
    return self.__balance

# Account1 will act as the object
account1 = BankAccount("87654321", 9999)

# Use the methods to get the data
print("Account Number: ", account1.gt_account_num())
print("Accounts' Balance: ", account1.gt_balance())

# Use the methods to set the data
account1.set_account_num(87654321)
account1.set_balance(9876)

# Display the updated data/information
print("Updated Account Number: ", account1.gt_account_num())
print("Updated Balance: ", account1.gt_balance())