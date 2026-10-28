# Class that reperesnts as a blueprint for bank accounts
# tells what a bank account should have and do
class BankAccount:


# attributes- which is created from that blueprint
# the accounts first information

## __init__ is the thing that gives the account its starting information
## self is the account being worked on
## accoun_num is the account number thats given to the account
## balance is the starting money, or the money inside the account as of the moment
## the = sign puts a value into a variable or attrivute such as account_num and balance
  def __init__(self, account_num, balance):
    self.__account_num = account_num
    self.__balance = balance

## setters and getters are methods of the actions that you can do to the account
# setters (changes information)
# self.__account_num and self.__balance acts as a save button where informations are saved to that specific account.
# lets you change the account num

  @account_num.setter
  def account_num(self, account_num):
    self.__account_num = account_num


# lets you change the balance of the account
# checks if balance is negative or positive, as the balance cannnot have a negative value
# the print statements displays a message weather the balance is negatice or positive 
  
  @balance.setter
  def balance(self, balance):
    if balance >= 0: 
       self.__balance = balance
    else:
      print("Balance cannot be negative.")


# getters (retrieves information)
# this lets you get or view the informations
# return means giving the value back
  @property
  def account_num(self):
    return self.__account_num

#access the method like an attribute 
  @property 
  def balance(self):
    return self.__balance

# this creates an account named "account1"
# the account num is 87654321 and the balance is 9999
account1 = BankAccount("87654321", 9999)


# this displlays the information
print("Account Number: ", account1.account_num)
print("Accounts' Balance: ", account1.balance)

# This changes the values of the account num and the balance
account1.account_num = "87654321"
account1.balance = 9876

# Displays the updated data/information
print("Updated Account Number: ", account1.account_num)
print("Updated Balance: ", account1.balance)


