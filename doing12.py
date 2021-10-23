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




two_heart= Card("Hearts", "Two")

three_of_clubs= Card("Clubs", "Three")


print("@@@@@@@@@@@@@@@@@@@@@@")



class Deck():

	def __init__(self):

		self.all_cards= []

		for suit in suits:
			for rank in ranks:
				#Create the card object
				created_card= Card(suit, rank)
				print(created_card)

				#why self here? Cuz its not being passed as parameter
				# https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/20662940#content
				# check above at 6:10
				self.all_cards.append(created_card)


	def shuffle(self): 

		random.shuffle(self.all_cards)

	def deal_one(self):
		return self.all_cards.pop()



new_deck= Deck()

mycard= new_deck.deal_one()


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


new_player= Player("Jose")

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print(new_player)

print(mycard)


new_player.add_cards(mycard)

print(new_player)


print("@@@@@@@@@@@@")
print(new_player.all_cards[0])


new_player.add_cards([mycard, mycard, mycard])

print(new_player)

new_player.remove_one()

print(new_player)
