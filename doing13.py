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


a= Chips()

take_bet(a)

print(a.)