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


import random

random_num= random.randint(0,100)
print(random_num)

r= True

guess_list= []

while True:
	answer=int((input("guess a number")))

	guess_list.append(answer)

	print(guess_list)
	print("@@@@@@")

	if  answer < 1 or 100 < answer:
		print("OUT OF BOUNDS")
	elif random_num- 10 <= answer and answer <= random_num+ 10:
		print("WARM!!")
	elif random_num- 10 > answer or answer> random_num+ 10:
		print("COLD!!")
	elif guess_list[-1] answer	#Come back

