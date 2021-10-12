

num = 13

if num> 1:

    for f in range(2, num//2+1):

        #If number is divisible by any number between 2 n num//2,
        #its not prime number
        if num%f == 0:
            print(f"this {num} not prime number")
            break

    print(f"this {num} issss prime number!!!")

