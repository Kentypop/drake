
# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/03-Function%20Practice%20Exercises.ipynb

"""
MASTER YODA: Given a sentence, return a sentence with the words reversed
"""

def yoda(sentence):
	splitted= sentence.split()

	reverse= splitted[::-1]

	result= " ".join(reverse)

	return result

print(yoda('I am home'))


# SOLUTION

# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/04-Function%20Practice%20Exercises%20-%20Solutions.ipynb

def master_yoda(text):
    return ' '.join(text.split()[::-1])


print(master_yoda('I am home'))