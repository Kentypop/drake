import json 

numbers= [2,3,4,5,6,7777777777]

filename= 'numbers.json'

with open(filename, 'w') as f:
	json.dump(numbers, f)



with open(filename, 'r') as e:
	print(e.read())	