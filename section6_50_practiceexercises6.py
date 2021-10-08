# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/03-Function%20Practice%20Exercises.ipynb

"""
ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
"""

def there(num):
	if 90<= num and num<= 110:
		return True
	elif 190<= num and num<= 210:
		return True
	else:
		return print("none the above")


print(there(209))



# SOLUTION
# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/04-Function%20Practice%20Exercises%20-%20Solutions.ipynb



def almost_there(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))


print(almost_there(80))