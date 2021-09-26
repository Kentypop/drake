def check_even(num):
	#return all the even numbers in a list
	newlist= []

	for f in num:
		if f%2== 0: 
			newlist.append(f)
		else:
			pass
	return newlist			


num= [1,2,3,4,5,6]

print(check_even(num))    

