class Account:
    
    def __init__(self, owner, balance):
    	self.owner= owner
    	self.balance= balance

    def __str__(self):
    	return f"Account ownver: {self.owner} \nAccount balance: {self.balance}"

    def deposit(self):

    	#get input
    	amount= int(input("how much u wanna deposit?"))

    	self.balance+= amount
    	print(f"Your total balance is {self.balance}")

    	return self.balance

    def withdraw(self):

    	amount= int(input("how much u wanna withdraw?"))

    	if amount > self.balance:
    		print(f"sry ur withraw {amount} exceeds {self.balance} balance")
    	else:
    		self.balance-= amount
    		print(f"your balacne ios now {self.balance}")

    	return self.balance







# 1. Instantiate the class
acct1 = Account('Jose',100)
# 2. Print the object
print(acct1)

acct1.withdraw()

print(acct1)