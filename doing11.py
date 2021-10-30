import random



suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}



class Card:

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


    class Chips:
    
    def __init__(self, total= 100):
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
	print("\n Dealer's hand: ")
	print("First card hidden!")
	print(dealer.cards[1])

	#Show all (2 cards) of the player's hand/cards


def show_all(player, dealer):

	#show all dealer's cards
	#calculate and display value(J+k == 20)

	#show al player's cards





test_deck= Deck()
test_deck.shuffle()


test_player= Hand()

pulled_card= test_deck.deal()
print(pulled_card)

test_player.add_card(pulled_card)
print(test_player.value)
