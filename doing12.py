

num = 14

for aye in range(0,num):
	#check if a number is prime
	if num> 1:

	    for f in range(2, num//2+1):

	        #If number is divisible by any number between 2 n num//2,
	        #its not prime number
	        if num%f == 0:
	            print(f"this {num}, {f} not prime number")
	            break

	        else:
	            print(f"this {num}, {f} issss prime number!!!")

