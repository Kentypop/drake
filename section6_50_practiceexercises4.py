# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/03-Function%20Practice%20Exercises.ipynb

"""
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
"""

def capital1_4(name):
	first= name[0].upper()
	fourth= name[3].upper()

	rest= name[1:]

	return first+fourth


print(capital1_4(name='abcdef'))


# SOLUTION

# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/04-Function%20Practice%20Exercises%20-%20Solutions.ipynb


def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short!'


print(old_macdonald('macdonald'))