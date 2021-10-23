"""
UNPACK tuple in class
"""

class Line:
    
    def __init__(self,coor1, coor2):
    	#Define coorinates
        self.coor1= coor1
        self.coor2= coor2
    
    def distance(self):
    	#unpack and calculate
    	x1, y1= self.coor1
    	print(x1)
    	print(y1)
    	x2, y2= self.coor2
    	return ((x2-x1)**2+(y2-y1)**2)**(1/2)
    
    def slope(self):
    	#unpack and calculate
        x1, y1= self.coor1
        x2, y2= self.coor2
        return (y2-y1)/(x2-x1)



coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

print(li.coor1)
print(li.coor2)


print(li.distance())
print(li.slope())


#Other way to unpack
class Line():   
    def __init__(self,coor1,coor2):
        #self.coor1 = coor1
        #self.coor2 = coor2
        self.x1, self.y1 = coor1
        self.x2, self.y2 = coor2
    def distance(self):
        return ((self.x2-self.x1)**2+(self.y2-self.y1)**2)**(1/2)
    def slope(self):
        return (self.y2-self.y1)/(self.x2-self.x1) 


"""
try and except
"""

try:
   You do your operations here...
   ...
except ExceptionI:
   If there is ExceptionI, then execute this block.
except ExceptionII:
   If there is ExceptionII, then execute this block.
   ...
else:
   If there is no exception then execute this block.
finally:
The finally: block of code will always be run regardless if there was an exception in the try code block. 


"""
error and exception handling
"""

try:
	#WANT to attempt this code
	#May have an error

	result= 10+ 10
except: 
	#execute when ERROR
	print("hey it looks like u arent adding corenylty")
else:
	#execute when NO ERROR
	print("Add went well!")
	print(result)
finally:
	print("I always run")

print("MUMMMMM")

# except: だけなら except for ANY error
except: 



try:
	f= open('testfile', 'r')
	f.write("Write a test line")
except TypeError:
	print("There was a type error!")
except:
	print("All other exception!!@@@@@@")
finally:
	print("I always run")



def ask_for_int():

	while True:
		try:
			result= int(input("Please provide number:"))
		except:
			print("whoops! thats not a number")
			continue
		else:
			print("Yes thank you")
			break
		finally:
			print("End of try/except/finally")
			print("I will always run at the end")


ask_for_int()


"""
unittest
"""

#doing12.py
def cap_text(text):
	return text.title()


#doing13.py
import unittest
import doing12


class TestCap(unittest.TestCase):

	def test_one_word(self):
		text= 'python'
		result= doing12.cap_text(text)
		self.assertEqual(result, 'Python')

	def test_multiple_words(self):
		text= 'monty python'
		result= doing12.cap_text(text)
		self.assertEqual(result, 'Monty Python')



if __name__ == '__main__':
	unittest.main()

"""
some class example
"""

class Account():

	#attribuet or owner and balance
	def __init__(self, owner, balance):
		self.owner= owner
		self.balance= balance


	def deposit(self, deposit):

		self.balance+= deposit
		return f"You have deposit: {deposit}, your balance is now {self.balance}"



	def withdraw(self, withdraw):
		
		#Withdraw if balance is more or the equal to withdrwa amount
		if self.balance>= withdraw:
			self.balance-= withdraw
			return f"You have withdraw: {withdraw}, your balance is now {self.balance}"
		else:
			return f"Your {withdraw} amunt exceeds {self.balance}"

	def __str__(self):
		return f"Account owner: {self.owner} \nAccount balance: {self.balance}"




ac= Account('Jose',100)

print(ac)
print("@@@@@@@")


print(ac.deposit(50))
print(ac.withdraw(75))

print(ac.withdraw(500))


"""
how import work
"""

from random import shuffle

shuffle(mylist)


import random

random.shuffle(mylist)