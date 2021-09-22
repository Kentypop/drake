import random

random_num= random.randint(0,100)

print(random_num)

r= True

while True:
	answer=int((input("guess a number")))
	print(answer)

	if  answer < 1 or 100 < answer:
		print("OUT OF BOUNDS")
	elif 	