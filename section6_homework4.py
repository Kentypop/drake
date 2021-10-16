# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/09-Functions%20and%20Methods%20Homework%20-%20Solutions.ipynb

"""
Functions and Methods Homework Solutions
Write a Python function that takes a list and 
returns a new list with unique elements of the first list.
"""

def unique_list(lst):
	a= set(lst)
	return list(a)


print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))


#solution

def unique_list(lst):
	return list(set(lst))

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))




def unique_list(lst):
    # Also possible to use list(set())
    x = []
    for a in lst:
        if a not in x:
            x.append(a)
    return x


unique_list([1,1,1,1,2,2,3,3,3,3,4,5])