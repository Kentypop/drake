import random



suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace': [1,11]}



class Card():

	def __init__(self, suit, rank): 	

		self.suit= suit
		self.rank= rank
		#Show num in int
		self.value= values[rank]

	def __str__(self):
		return self.rank + "of" + self.suit + "  " + str(self.value)



class Deck():

	#All cards
	def __init__(self):

		self.all_cards= []

		for suit in suits:
			for rank in ranks:

				#Create card object
				created_card= Card(suit, rank)
				#Put all the card Object in list
				self.all_cards.append(created_card)


	#Shuffle
	def shuffle(self): 
		random.shuffle(self.all_cards)

	#Deal one
	def deal_one(self):
		return self.all_cards.pop(0)


class Player():

	#bank roll
	#Actions hit or stay
	#player cards
	def __init__(self, bankroll):

		self.bankroll= bankroll
		self.player_cards= []


	#Hit or stay, also simply adding cards
	def add_cards(self, new_cards):
		if type(new_cards) == type([]):
			#list of multiple Card objects
			self.player_cards.extend(new_cards)
		else:
			#For a single card object
			self.player_cards.append(new_cards)

	def bet(self, number):
		if int(number) < self.bankroll:
			self.bankroll-= int(number)
		else:
			print("not enough. pick again.")





print("@@@@@@@@@@@@@")
cc= Card(suits[0], ranks[0])

print(cc)

print(cc.value)

a= Deck()
print(a)
print("@@@@@@@@@@@@@")


#SET UP
player= Player(1000)
dealer= Player(0)

new_deck= Deck()
new_deck.shuffle()

#Two card at the start of game
player.add_cards(new_deck.deal_one())
player.add_cards(new_deck.deal_one())

#Two card at the start of game
dealer.add_cards(new_deck.deal_one())
dealer.add_cards(new_deck.deal_one())

game_on= True



#Display
print("Dealer Card: ")
for f in dealer.player_cards[1:]:
	print(f"{f}\n")
	
print("Your card")
for f in player.player_cards:
	print(f"{f}\n")
		#if 'Ace' in f:
		#	choose= input("You have Ace, press 0 for 1, 1 for 11. ")


mylist= []

print("Your card")
for f in player.player_cards:
	print(f"{f}\n")
	print(f.value)
	if f.value == [1,11]:
		num= input("0 or 1?")
		f.value= f.value[int(num)]

	mylist.append(f.value)
	print(sum(mylist))

print(mylist)
#print(sum(mylist))

