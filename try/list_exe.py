#Write a Python program to sum all the items in a list.

a= [1,2,50]

sumtotal= 0

for f in a:
	print(f)
	sumtotal+= f

print(sumtotal)
print("@@@@@@\n\n")



def sum_list(items):
	sum_numbers= 0

	for f in items:
		sum_numbers+= f

	return sum_numbers

print(sum_list([1,2,3]))
print("@@@@@@\n\n")	


#Write a Python program to multiply all the items in a list.

