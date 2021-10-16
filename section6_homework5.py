# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/09-Functions%20and%20Methods%20Homework%20-%20Solutions.ipynb

"""
Functions and Methods Homework Solutions
Write a Python function to multiply all the numbers in a list.
"""


def multiply(numbers):  

	total= 1

	for f in numbers:
		result= f * total

	return print(result)
		


multiply([1, 2, 3, -4])



#solution


def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total

multiply([1,2,3,-4])