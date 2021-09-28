# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/03-Function%20Practice%20Exercises.ipynb

"""
MAKES TWENTY: Given two integers, 
return True if the sum of the integers is 20 or if one of the integers is 20. 
If not, return False
"""

def twenty(n1, n2):
	if n1== 20 or n2 == 20:

		return True

	elif n1+n2 == 20:

		return True

	else:
		return False



print(twenty(20, 10))
print(twenty(12, 8))
print(twenty(2,3))

print("\n")
# SOLUTION

# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/04-Function%20Practice%20Exercises%20-%20Solutions.ipynb

def makes_twenty(n1,n2):
    return (n1+n2)==20 or n1==20 or n2==20

print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))