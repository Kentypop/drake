#method chain


>>> text[::-1].split()
['pus', 'yas', '1relyt']
>>> text.split()[::-1]
['sup', 'say', 'tyler1']

"""
which one is 'best practice'?
"""

def yoda(sentence):
	splitted= sentence.split()

	reverse= splitted[::-1]

	result= " ".join(reverse)

	return result

print(yoda('We are ready'))



def master_yoda(text):
    return ' '.join(text.split()[::-1])


print(master_yoda('I am home'))



@@@@@

# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/03-Function%20Practice%20Exercises.ipynb

"""
LEVEL 2 PROBLEMS
FIND 33:
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
"""


def get_33(numbers):
	emp_list= [0]

	for f in numbers:

		emp_list.append(f)

		print(f)
		print(emp_list)
		print("@@@@@@@@@")

		if f== 3 and emp_list[-2]== 3:
			return True
		else:
			pass


print(get_33([3, 1, 3]))


# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/04-Function%20Practice%20Exercises%20-%20Solutions.ipynb

# SOLUTION

def has_33(nums):
	#@@@@@@@@@@@@@ whats up with the -1?
    for i in range(0, len(nums)-1):
      
        # nicer looking alternative in commented code
        #if nums[i] == 3 and nums[i+1] == 3:
    
        if nums[i:i+2] == [3,3]:
            return True  
    
    return False



print(has_33([1, 3, 3]))