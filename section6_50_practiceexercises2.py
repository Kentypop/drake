# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/03-Function%20Practice%20Exercises.ipynb

"""
ANIMAL CRACKERS: Write a function takes a two-word string 
and returns True if both words begin with same letter
"""

def same_letter(a):
	splitted= a.split()
	print(splitted)

	if splitted[0][0]== splitted[1][0]:

		return True

	else:

		return False


yo= same_letter('ian ie')
print(yo)



# SOLUTION

# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/04-Function%20Practice%20Exercises%20-%20Solutions.ipynb

def animal_crackers(text):
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]


print(animal_crackers('aevelheaded Llama'))
