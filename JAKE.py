# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/03-Function%20Practice%20Exercises.ipynb

"""
LEVEL 2 PROBLEMS

SUMMER OF '69: Return the sum of the numbers in the array, 
except ignore sections of numbers starting with a 6 
and extending to the next 9 (every 6 will be followed by at least one 9).
 Return 0 for no numbers.
"""


def summer_69(aa):
    
    total= 0

    for f in aa:
        if f== 6 or f== 9:
            continue
        total+= f

    return total


print(summer_69([2, 1, 6, 9, 11]))


#SOLUTION
def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total

print(summer_69([4, 5, 6, 7, 8, 9])) 