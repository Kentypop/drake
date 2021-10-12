# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/03-Function%20Practice%20Exercises.ipynb

"""
CHALLENGING PROBLEMS

SPY GAME: Write a function that takes in a list of integers 
and returns True if it contains 007 in order
"""

def spy_game(nums):

    mylist= []


    for f in nums:
        if f== 0:
            mylist.append(f)
        elif f== 7:
            mylist.append(f)

    print(mylist)
    
    if mylist== [0, 0, 7]:
        return True
    else:
        return False  



print(spy_game([1,0,2,4,0,5,7])) 


#SOLUTION

def spy_game(nums):

    code= [0,0,7,'x']

    for num in nums:
        if num== code[0]:
            code.pop(0)

    return len(code)== 1




print(spy_game([1,2,4,0,0,7,7]))