# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/03-Function%20Practice%20Exercises.ipynb

"""
LEVEL 2 PROBLEMS

PAPER DOLL: Given a string, 
return a string where for every character in the original there are three characters
"""

def paper_doll(text):
	added= ''

	for f in text:
		#two_copy = f*2
		#added= f+two_copy
		print(f)

		added= added.join(f*3)
		print(added)
		print("@@@@@")

	return added


print(paper_doll("aHello"))

def paper_doll(text):
	added= ''

	for f in text:
		two_copy = f*3
		added= added+two_copy


	return added


print(paper_doll("Hello"))



# SOLUTION

def paper_doll(text):
    result = ''
    for char in text:
        result += char * 3
    return result

paper_doll('Hello')