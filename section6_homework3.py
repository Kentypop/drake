# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/09-Functions%20and%20Methods%20Homework%20-%20Solutions.ipynb

"""
Functions and Methods Homework Solutions
Write a Python function that accepts a string and
calculates the number of upper case letters and lower case letters.
"""

def up_low(s):
    list_up= []
    list_low= []


    for f in s.split():
    	if f[0].isupper() == True:
    		list_up.append(f[0])
    		list_low.append(f[1:])
    		joined= ''.join(list_low)


    		print(list_up)

    	elif f.islower() == True:
    		list_low.append(f)
    		joined= ''.join(list_low)

    print(joined)
    ups= len(list_up)		
    lows= len(joined)

    print(f"we got {ups} and {lows}")

    return ups, lows


up_low('Hello Mr. Rogers, how are you this fine Tuesday?')


#solution

def up_low(s):

	lowercase= 0
	uppercase= 0

	for char in s:
		if char.isupper():
			uppercase+= 1
		elif char.islower():
			lowercase+= 1
		else:
			pass

	print(f"original string: {s}")
	print(f"Lower case count: {lowercase}")
	print(f"Upper case count: {uppercase}")	



up_low('Hello Mr. Rogers, how are you this fine Tuesday?')




def up_low(s):
	d= {'upper':0, 'lower': 0}


	for char in s:
		if char.isupper():
			d['upper']+= 1
		elif char.islower():
			d['lower']+= 1
		else:
			pass

	print(f"original string: {s}")
	print(f"Lower case count: {d['lower']}")
	print(f"Upper case count: {d['upper']}")	



up_low('Hello Mr. Rogers, how are you this fine Tuesday?')