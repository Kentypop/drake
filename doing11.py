suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

ll= []


for suit in suits:
	print(suit)
	for rank in ranks:
		print(rank)
		ll.append(rank)


print(ll)
