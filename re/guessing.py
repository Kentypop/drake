"""
Guessing Game Challenge
Let's use while loops to create a guessing game.

The Challenge:

Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
On a player's first turn, if their guess is
within 10 of the number, return "WARM!"
further than 10 away from the number, return "COLD!"
On all subsequent turns, if a guess is
closer to the number than the previous guess return "WARMER!"
farther from the number than the previous guess, return "COLDER!"
When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!
"""

# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/02-Python%20Statements/09-Guessing%20Game%20Challenge.ipynb

import random

random_num= random.randint(0,100)
print(random_num)


guess_list= [0]

while True:
	answer=int((input("guess a number")))

	guess_list.append(answer)

	print(guess_list)
	print("@@@@@@")
	#Newest answer
	print(guess_list[-1])
	print("@@@@@@")


	if  answer < 1 or 100 < answer:
		print("OUT OF BOUNDS")

	if answer== random_num:
		print(f'CONGRATS ITS f{answer}')
		break	

	elif abs(random_num- guess_list[-2]) > abs(random_num- answer):
		print("WARMER!")

		print(abs(answer- guess_list[-2]))
		print(abs(answer- guess_list[-1]))

	elif abs(random_num- answer) > 	abs(random_num- guess_list[-2]):
		print("COLDER")


	elif random_num- 10 <= answer and answer <= random_num+ 10:
		print("WARM!!")

	elif random_num- 10 > answer or answer> random_num+ 10:
		print("COLD!!")


