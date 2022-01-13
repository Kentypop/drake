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

import random



suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True



class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck():
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    
    def __str__(self):
        deck_comp= ''
        for card in self.deck:
            deck_comp+= '\n' + card.__str__()
        return "The deck has:" +deck_comp


    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card= self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
    	#card passed in
    	#from Deck.deal() --> single Card(suit, rank)
        self.cards.append(card)
        self.value+= values[card.rank]

        #track aces
        if card.rank == 'Ace':
        	self.aces+= 1
    
    def adjust_for_ace(self):
        
        #IF TOTAL VALUE> 21 AND I STILL HAVE AN ACE
        #THEN CAHNGE MY ACE TO BE A 1 INSTEAD OF AN 11
        while self.value > 21 and self.aces:
        	self.value-= 10
        	self.aces-= 1



class Chips():
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total+= self.bet
    
    def lose_bet(self):
        self.total-= self.bet



def take_bet(chips):

	while True:

		try:
			chips.bet= int(input("How many chips would you like to bet?"))
		except:
			print("Sorry please provide an int")
		else:
			if chips.bet > chips.total:
				print(f"Sorry, you do not have enough chips! You have {chips.total}")
			else:
				break



def hit(deck, hand):

	single_card= deck.deal()
	hand.add_card(single_card)
	hand.adjust_for_ace()



def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        
        if x[0].lower() == 'h':
            hit(deck,hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break


def show_some(player, dealer):

	#dealer.cards[0]

	#Show only ONE of the dealer's cards
	print("\nDealer's hand: ")
	print("First card hidden!")
	print(dealer.cards[1])

	#Show all (2 cards) of the player's hand/cards
	print("\nPlayer's hand:")
	for card in player.cards:
		print(card)


def show_all(player, dealer):

	#show all dealer's cards
	print("\n Dealer's hand:")
	for card in dealer.cards:
		print(card)
	#calculate and display value(J+k == 20)
	print(f"Value of Dealer's hand is: {dealer.value}")

	#show al player's cards
	print("\n Player's hand:")
	for card in player.cards:
		print(card)

	print(f"Value of Player's hand is: {player.value}")



def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")




while True:
	#Print an opening statement

	print("WELCOME TO BLACKJACK")
	#Create & shuffle the deck, deal two cards to each player
	deck= Deck()
	deck.shuffle()

	player_hand= Hand()
	player_hand.add_card(deck.deal())
	player_hand.add_card(deck.deal())

	dealer_hand= Hand()
	dealer_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())

	#Set up the Player's chips 
	player_chips= Chips()

	#Prompt the Player for their bet
	take_bet(player_chips)

	#Show cards(but keep one dealer card hiddden)
	show_some(player_hand, dealer_hand)

	while playing: #recall this variable from our hit_or_stand function

		#Prompt for Player to Hit or Stand
		hit_or_stand(deck, player_hand)

		#Show cards (but keep one dealer card hidden)
		show_some(player_hand, dealer_hand)

		#If player's hand exceeds 21, run opkayer_busts() and make out of loop
		if player_hand.value> 21:
			player_busts(player_hand, dealer_hand, player_chips)

			break

	#If Player hasn't busted, play Dealer's hand until Dealer reaches 17
	if player_hand.value<= 21:

		while dealer_hand.value < 17:
			hit(deck, dealer_hand)

		#Show all cards
		show_all(player_hand, dealer_hand)

		#Run different winning scenarios
		if dealer_hand.value > 21:
			dealer_busts(player_hand, dealer_hand, player_chips)

		elif dealer_hand.value > player_hand.value:
			dealer_wins(player_hand, dealer_hand, player_chips)

		elif dealer_hand.value < player_hand.value:
			player_wins(player_hand, dealer_hand, player_chips)
		else:
			push(player_hand, dealer_hand)

	#Inform Player of their chips total
	print(f"\n Player total chips area at: {player_chips.total}")
	#Ask to play again
	new_game= input("Would you like to play another hand? y/n")

	if new_game[0].lower() == 'y':
		playing= True
		continue
	else:
		print("Thank you for playing!")
		break