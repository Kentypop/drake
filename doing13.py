def count_primes(num):

	#Check for 0 or 1 input
	if num< 2:
		return 0

	#########
	# 2 or greater
	#########

	#Store prime numbers
	primes= [2]

	#Counter going yp to input num
	x= 3

	# x is going through every number up to input num
	while x<= num:
		#Check if x is prime
		for y in range(3,x,2):
			if x%y == 0:
				x+= 2
				break
		else:
			primes.append(x)
			x+= 2

	print(primes)
	return len(primes)


print(count_primes(7))


