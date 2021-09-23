
#Write a program that prints the integers from 1 to 100. 
#But for multiples of three print "Fizz" instead of the number, 
#and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".


for f in range(0,101):

	if f%3 == 0 and f%5 == 0:
		print(f"fizzbuzzz {f}")
	elif f%3 == 0:
		print(f"Fizz {f}")
	elif f%5 == 0:
		print(f"Buzz {f}")
	else:
		print(f"{f}")	