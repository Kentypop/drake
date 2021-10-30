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



"""
Milestone project 2 section warmup
"""

#CARD
import random 



suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}



class Card():

	def __init__(self, suit, rank):
		self.suit= suit
		self.rank= rank
		self.value= values[rank]

	def __str__(self):
		return self.rank + " of " + self.suit




class Deck():

	def __init__(self):

		self.all_cards= []

		for suit in suits:
			for rank in ranks:
				#Create the card object
				created_card= Card(suit, rank)
				#print(created_card)

				#why self here? Cuz its not being passed as parameter
				# https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/20662940#content
				# check above at 6:10
				self.all_cards.append(created_card)


	def shuffle(self): 

		random.shuffle(self.all_cards)

	def deal_one(self):
		return self.all_cards.pop()




class Player():


	def __init__(self, name):

		self.name= name
		self.all_cards= []


	def remove_one(self):
		return self.all_cards.pop(0)


	def add_cards(self, new_cards):
		if type(new_cards) == type([]):
			#list of multiple Card objects
			self.all_cards.extend(new_cards)
		else:
			#For a single card object
			self.all_cards.append(new_cards)


	def __str__(self):
		return f"Player {self.name} has {len(self.all_cards)} cards"





#GAME SETUP

player_one= Player("One")
player_two= Player("Two")

new_deck= Deck()
new_deck.shuffle()


for x in range(26):
	player_one.add_cards(new_deck.deal_one())
	player_two.add_cards(new_deck.deal_one())


game_on= True


#I'm testing stuff
print("\n@@@@@@@@@@@@@@@@@@@")

print(len(player_one.all_cards))
print(player_one.all_cards)

for f in player_one.all_cards:
	print(f)

print("@@@@@@@@@@@@@@@@@@@\n")




round_num = 0
while game_on:
    
    round_num += 1
    print(f"Round {round_num}")
    
    # Check to see if a player is out of cards:
    if len(player_one.all_cards) == 0:
        print("Player One out of cards! Game Over")
        print("Player Two Wins!")
        game_on = False
        break
        
    if len(player_two.all_cards) == 0:
        print("Player Two out of cards! Game Over")
        print("Player One Wins!")
        game_on = False
        break
    
    # Otherwise, the game is still on!
    
    # Start a new round and reset current cards "on the table"
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    
    at_war = True

    while at_war:


        if player_one_cards[-1].value > player_two_cards[-1].value:

            # Player One gets the cards
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            
            
            # No Longer at "war" , time for next round
            at_war = False
        
        # Player Two Has higher Card
        elif player_one_cards[-1].value < player_two_cards[-1].value:

            # Player Two gets the cards
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            
            # No Longer at "war" , time for next round
            at_war = False

        else:
            print('WAR!')
            # This occurs when the cards are equal.
            # We'll grab another card each and continue the current war.
            
            # First check to see if player has enough cards
            
            # Check to see if a player is out of cards:
            if len(player_one.all_cards) < 5:
                print("Player One unable to play war! Game Over at War")
                print("Player Two Wins! Player One Loses!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Player Two unable to play war! Game Over at War")
                print("Player One Wins! Player One Loses!")
                game_on = False
                break
            # Otherwise, we're still at war, so we'll add the next cards
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())



"""
args, kwargs
"""

def myfunc(*args, **kwargs):

	print(args)
	print(kwargs)
	print(f"I would like {args[0]} {kwargs['food']}")


myfunc(10,20,30, fruit='orange', food='eggs', animal='dog')


def view(*args, **kwargs):
	

	print(f"{kwargs}")


my_kwargs = dict(hello='world',star='wars')

view(**my_kwargs)




"""
0 AND OTHER NUMBER
python truthiness
"""

While any non-zero value is treated as true, None and 0 are interpreted as false by Python.


python truthiness
link: 10:00    95. soolution to milesotne p
https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/9497654#notes