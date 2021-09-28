# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/03-Function%20Practice%20Exercises.ipynb

"""
LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers 
if both numbers are even, but returns the greater if one or both numbers are odd
"""

def lesser_of_two_evens(num1, num2):
	if num1%2 != 0 or num2%2 != 0:
		result= max(num1, num2)
		print(result)

		return result

	elif num1< num2 or num2< num1:
		result= min(num1, num2)
		print(result)

		return result




result= lesser_of_two_evens(2,4)


#SOLUTION
# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/04-Function%20Practice%20Exercises%20-%20Solutions.ipynb

def lesser_of_two_evensYE(a, b):
	if a%2== 0 and b%2 == 0:
		print(min(a,b))
		return min(a,b)

	else:
		print(max(a,b))
		return max(a,b)


lesser_of_two_evensYE(2,5)