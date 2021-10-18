# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/09-Functions%20and%20Methods%20Homework%20-%20Solutions.ipynb

"""
Functions and Methods Homework Solutions
Write a Python function that checks whether a word or phrase is palindrome or not.
"""

def palindrome(s):

	if s.replace(" ", "") == s.replace(" ", "")[::-1]:

		print(s.replace(" ", ""))
		print(s.replace(" ", "")[::-1])
		print("ayeaye")
		
		return True
	else:
		print("aaaaaaaa")

palindrome("nurses run")


#soluton

ef palindrome(s):
    
    s = s.replace(' ','') # This replaces all spaces ' ' with no space ''. (Fixes issues with strings that have spaces)
    return s == s[::-1]   # Check through slicing

palindrome('nurses run')
