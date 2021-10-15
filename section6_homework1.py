# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/09-Functions%20and%20Methods%20Homework%20-%20Solutions.ipynb

"""
Functions and Methods Homework Solutions
Write a function that computes the volume of a sphere given its radius.
"""

def vol(rad):
	v= 4/3 * 3.14 * rad**3
	return v


print(vol(2))

#solution
def vol(rad):
    return (4/3)*(3.14)*(rad**3)

# Check
vol(2)