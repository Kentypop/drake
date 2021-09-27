"""
Modulo or "Mod" Operator. Find the remainder usinbg %
Check to see fi a number is EVEN or not by % ". If 0 then its even
"""
>>> 9%4
>>> 1

"""
String, slicing and indexing
"""
>>> mystring= "hello world"
>>> mystring[::]

#Reverse a string
>>> mystring= "hello world"
>>> mystring[::-1]

#String immutability workaround
>>> name= "Sam"
>>> last_letters= name[1::]
>>> last_letters
'am'
>>> 'P'+ last_letters
'Pam'

>>> s= "my momo"
>>> s.split('m')
['', 'y ', 'o', 'o']

#float formatting
>>> a= 10/7
>>> a
1.4285714285714286
>>> print(f"{a:1.3f}")
1.429


"""
Sort list
Don't return anything cuz it sort list IN PLACE.
When you called back, its sorted.
"""

>>> a= [1,2,3,4]
>>> a.append("YOLO")
>>> a
[1, 2, 3, 4, 'YOLO']


mylist= ["koko", "ash", "yuna"]
mylist.sort()


"""
Tuple unpacking
"""
list2 = [(2,4),(6,8),(10,12)]

for a,b in list2:
	print(a)
	print(b)


"""
Sets
"""
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Sets are useful for getting the unique value
>>> mylist= [1,1,1,2,2,2]
>>> mylist
[1, 1, 1, 2, 2, 2]
>>> set(mylist)
{1, 2}


"""
I/O with Basic file  
"""

f= open("trying.txt", "a")
f.write("supsup")

f.close()

f= open("trying.txt", "r")
print(f.read())


#BETTER way than ^^^
with open("trying.txt", "r") as myfile:
	print(myfile.read())



"""
For loop
"""
>>> list_sum= 0
>>> mylist= list(range(0,10))
>>> mylist
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> for num in mylist:
...     list_sum= list_sum + num
...
>>> print(list_sum)
45

#UNDERSCORE in loop, whe you dont wanna use variable
mylist= ["koko", "ash", "yuna"]

for _ in mylist:
	print("yea!")


"""
ENUMERATE, this operation so common they have enumerate()
"""
>>> index= 0
>>> for f in 'abcde':
...     print(f"At index {index} the letter is {f}")
...     index+= 1
...
At index 0 the letter is a
At index 1 the letter is b
At index 2 the letter is c
At index 3 the letter is d
At index 4 the letter is e	


#Enumerate, in the fomr of tuple
>>> word= 'abcde'
>>> for f in enumerate(word):
...     print(f)
...
(0, 'a')
(1, 'b')
(2, 'c')
(3, 'd')
(4, 'e')


>>> for f,j in enumerate(word):
...     print(f)
...     print(j)
...     print()
...
0
a

1
b

2
c

3
d

4
e

"""
zip()
"""
>>> mylist1= [1,2,3]
>>> mylist2= ['a','b','c']
>>> zip(mylist1, mylist2)
<zip object at 0x0000024AB6826440>
>>> for f in zip(mylist1, mylist2):
...     print(f)
...
(1, 'a')
(2, 'b')
(3, 'c')

"""
IN, minx(), max(),
"""
>>> x in [1,2,3]
False

>>> list1= [1,10,100]
>>> min(list1)
1
>>> max(list1)
100
>>>


"""
INPLACE, and shuffle().
SECTION 5, 37  time: 12:20
"""
>>> from random import shuffle
>>> list1
[1, 10, 100]
>>> shuffle(list1)
>>> list1
[1, 100, 10]
#This is inplace function, meaning it operates inplace on that list
>>> random_list= shuffle(list1)
>>> random_list
>>> type(random_list)
<class 'NoneType'>
>>> list1
[1, 100, 10]
>>>


"""
randint()
"""
>>> from random import randint
>>> randint(0,100)
43
>>> randint(0,100)
32
>>> mynum= randint(0,100)
>>> mynum
60

""""
LIST COMPREHENSION
It is a unique way of quickly creating a list with python.
If you find yourseld using a for loop along with .append() to create a list, 
list comprehensionss are good alternative!
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

>>> mylist= [x for x in range(0,11)]
>>> mylist
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#Check even number
>>> mylist= [x for x in range(0,11) if x%2==0]
>>> mylist
[0, 2, 4, 6, 8, 10]


"""
Function
"""

#Provide a default value in the parameter
>>> def say_hello(name="seannn"):
...     print(f"hi daddy {name}")
... 
>>> say_hello()
hi daddy seannn
>>> say_hello(2222)
hi daddy 2222


#using return and not using return
>>> def print_result(a,b):
...     print(a+ b)
... 
>>> def return_results(a,b):
...     return a+ b
... 
>>> print_result(10,20)
30
>>> result= print_result(10,20)
30
>>> result
>>> 
>>> type(result)
<class 'NoneType'>
>>> return_results(10,20)
30
>>> result= return_results(10,20)
>>> result
30


>>> def myfunc(a,b):
...     print(a+b)
...     return a+b
... 
>>> result= myfunc(10,20)
30



"""
Positional argument
"""

#If you want to work with multiple positional argument in the sum, 
#you have to pass them in as tuple
>>> def myfunc(a,b):
...     return sum((a,b))* 0.05
... 
>>> myfunc(40, 60)
5.0

#What if we awnt to work with more than two number?
#One way is to assign alot of parameter
#This is cdefault is 0, if they dont pass stuff its 0, it wont affect the sum()
def myfunc(a,b, c=0):


# (*args) allow you to treat this as a tuple of parameters that are coming in
#whatevere this parameter is, user can pass in as many as want.
#and its going to be treated as tuple in that function
#you can loop thru it or iterate thru it or sum it together
#by convention u u use args. as long its followed by asterisk *
#It allow you to pass in as many argument as you want

>>> def myfunc(*args):
...     return sum(args)* 0.05
... 
>>> myfunc(40,60)
5.0
>>> myfunc(40,60,100,1000)
60.0
>>> 


>>> def myfunc(*args):
...     print(args)
... 
>>> myfunc(40,60,100,1000)
(40, 60, 100, 1000)



>>> def myfunc(*args):
...     for item in args:
...             print(item)
... 
>>> myfunc(40,60,100,1000)
40
60
100
1000

# python offers a way to handle arbitrarily number of keyworded argument
# **kwargs
# *args returns tuple
# **kwargs return a dictionary
#USE "" so it don fuck it up when you ['']

# (*args, **kwargs) when pass, has to be in order, CANNOT myfunc(1,2,3, girl='chick', boy='boi', 123)

>>> def myfunc(**kwargs):
...     if 'fruit' in kwargs:
...             print(f'My fruit of choice is {kwargs['fruit']}')
...     else:
...             print('I did not find any fruit here')
... 
>>> myfunc(fruit='apple')
My fruit of choice is {'fruit': 'apple'}



>>> def myfunc(**kwargs):
...     if 'fruit' in kwargs:
...             print('My fruit of choice is {}'.format(kwargs['fruit']))
...     else:
...             print('I did not find any fruit here')
... 
>>> myfunc(fruit= 'apple')
My fruit of choice is apple


>>> def myfunc(**kwargs):
...     print(kwargs)
... 
>>> myfunc(fruit='apple', veggie='lettuce')
{'fruit': 'apple', 'veggie': 'lettuce'}
