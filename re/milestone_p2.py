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

#player "int" card list
player_list= []

#dealer "int" card list
dealer_list= [] 


#LOGIC
while game_on:

	print(f"Your bankroll is {player.bankroll}")

	#Pick bet
	num= input("How much do you wanna bet?")
	player.bet(num)
	print(f"Your bet is : {num}")
	print(f"Amount left: {player.bankroll}")

	#Display
	print("Dealer Card: ")
	for f in dealer.player_cards:
		print(f"{f}\n")
		
	#Display and check sum
	print("Your card")
	for f in player.player_cards:
		print(f"{f}\n")

		#Pick num for Ace
		if f.value == [1,11]:
			num= input("Press 0 for 1 and 1 for 11?")
			f.value= f.value[int(num)]

			print(f"{f.value}\n")

		#Calculate tolal value of a player
		player_list.append(f.value)
		player_sum= sum(player_list) 

		if player_sum > 21:
			print("You lost mate")
			game_on= False

	print(f"Your total now is {player_sum}")

	turn= True

	while turn:

		#hit or stay
		decision= input("hit or stay?")

		if decision == 'hit':
			player.add_cards(new_deck.deal_one())

			#Check if over 21 or.
			#Display and check sum
			print("Your card")
			for f in player.player_cards:
				print(f"{f}\n")

				#Pick num for Ace
				if f.value == [1,11]:
					num= input("0 or 11?")
					f.value= f.value[int(num)]

					print(f"{f.value}\n")

				#Calculate tolal value of a player
				player_list.append(f.value)
				player_sum= sum(player_list)

				if player_sum > 21:
					print("You lost mate BUST")
					game_on= False
					turn= False
					break

			print(f"Your total now is {player_sum}")

				


		elif decision == 'stay':
			print(new_deck)

			dealer_turn= True

			while dealer_turn:
				#Enemy keep drawing 
				dealer.add_cards(new_deck.deal_one())

				#Check if over 21 or. or either beat me
				#Display and check sum
				print("Dealer card")
				for f in dealer.player_cards:
					print(f"{f}\n")

					#Pick num for Ace
					if f.value == [1,11]:
						num= input("0 or 11?")
						f.value= f.value[int(num)]

						print(f"{f.value}\n")

					#Calculate tolal value of a player
					dealer_list.append(f.value)
					dealer_sum= sum(dealer_list) 

					print(f"DEALER total now is {dealer_sum}")

					if dealer_sum > 21:
						print("Dealer lost. You won mate!")
						game_on= False
						turn= False
						dealer_turn= False
						break

					elif player_sum < dealer_sum < 21:
						print("YOU LOST")
						game_on= False
						turn= False
						dealer_turn= False
						break


		else:
			print("type again properly")






##SOLUTION @@@@@@@@@@@@@@@@@@@@@