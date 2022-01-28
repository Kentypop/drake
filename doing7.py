import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}



class Card:

	def __init__(self, suit, rank):
		self.suit= suit
		self.rank= rank
		self.value= values[rank]

	def __str__(self):
		return self.rank + " of " + self.suit



class Deck:

	def __init__(self):

		self.all_cards= []

		for suit in suits:
			for rank in ranks:
				#Create the card objects
				created_card= Card(suit,rank)

				self.all_cards.append(created_card)

	def shuffle(self):

		random.shuffle(self.all_cards)

	def deal_one(self):
		return self.all_cards.pop()



class Player:

	def __init__(self, name):
		self.name= name
		self.all_cards= []

	def remove_one(self):
		return self.all_cards.pop(0)

	def add_cards(self,new_cards):
		if type(new_cards) == type([]):
			self.all_cards.extend(new_cards)
		else:
			self.all_cards.append(new_cards)

	def __str__(self):
		return f"Player {self.name} has {len(self.all_cards)} cards."



new_deck= Deck()

print(new_deck.all_cards[-1])

new_deck.shuffle()

onee= new_deck.deal_one()

print(onee)

new_player= Player("Jose")

print(new_player)

new_player.add_cards(onee)

print(new_player)

print(new_player.all_cards[0])

new_player.add_cards([onee, onee,onee])

print(new_player)