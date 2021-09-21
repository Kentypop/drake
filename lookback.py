
"""
Sort list
Don't return anything cuz it sort list IN PLACE.
When you called back, its sorted.
"""
mylist= ["koko", "ash", "yuna"]

mylist.sort()


"""
UNDERSCORE in loop, whe you dont wanna use variable
"""
mylist= ["koko", "ash", "yuna"]

for _ in mylist:
	print("yea!")


"""
Tuple unpacking
"""
list2 = [(2,4),(6,8),(10,12)]

for a,b in list2:
	print(a)
	print(b)


""""
LIST COMPREHENSION
It is a unique way of quickly creating a list with python
Using for loop along with append() to create list 
"""
mystring= 'hello'

mylist= []

for f in mystring:
	mylist.append(f)

mylist	

#LISTCOMPREHENSION
mylist= [f for f in mystring]

#EXP 2
mylist= [x for x in 'word']