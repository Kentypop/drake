"""
Modulo or "Mod" Operator. Find the remainder usinbg %
Check to see if a number is EVEN or not by % ". If 0 then its even
"""
>>> 9%4
>>> 1

"""
() in calculation
() parenthesis prioritiize arithmetic
"""
>>> 2+3*2+3
11
>>> (2+3) * (2+3)
25

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
dictionary access
"""

>>> d= {'k1':123, 'k2': [0,1,2], 'k3':{'insidekey':100}}
>>> d['k3']
{'insidekey': 100}
>>> d['k3']['insidekey']
100
>>> d['k2'][2]
2
>>> d['k2'][0]
0


"""
How do I index a nested list? For example if I want to grab 2 from [1,1,[1,2]]?

NESTED LIST
"""
>>> a= [1,1,[1,2]]
>>> a[2][1]
2

"""
Tuple unpacking
"""
list2 = [(2,4),(6,8),(10,12)]

for a,b in list2:
	print(a)
	print(b)

for (a,b) in list2:

    SAME THING


>>> d= {'k1':1, 'k2':2, 'k3':3}
>>> for f in d.items():
...     print(f)
...
('k1', 1)
('k2', 2)
('k3', 3)

items() returns tuple. there fpore you can use tuple unpacking.

>>> for key,value in d.items():
...     print(key)
...     print(value)
...
k1
1
k2
2
k3
3
>>>

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
Tuple unpacking with function
"""

work_hours = [('Abby',100),('Billy',400),('Cassie',800)]


def employee_check(work_hours):
    
    # Set some max value to intially beat, like zero hours
    current_max = 0
    # Set some empty value before the loop
    employee_of_month = ''
    
    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    
    # Notice the indentation here
    return (employee_of_month,current_max)



employee_check(work_hours)    

('Cassie', 800)
#Since it return tuple, u can use the tuple unpacking to define


name, hours= employee_check(work_hours)


name
'Billy'
hours
4000

"""
Positional argument
"""

#If you want to work with multiple positional argument in the sum, 
#you have to pass them in as tuple
#@@@@@@@@@@@@@@@@@@@ ((a,b)) NECAUSE (a,b) is a tuple
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
...             print(f"My fruit of choice is {kwargs['fruit']}")
...     else:
...             print('I did not find any fruit here')
... 
>>> myfunc(fruit='apple')
My fruit of choice is apple


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


#method chain

>>> text= 'tyler1 say sup'

>>> text[::-1].split()
['pus', 'yas', '1relyt']
>>> text.split()[::-1]
['sup', 'say', 'tyler1']



"""
the use of SLICE @@@@
"""

# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/04-Function%20Practice%20Exercises%20-%20Solutions.ipynb

# SOLUTION

def has_33(nums):
	#@@@@ whats up with this -1?
    for i in range(0, len(nums)-1):
      
        # nicer looking alternative in commented code
        #if nums[i] == 3 and nums[i+1] == 3:
    
        if nums[i:i+2] == [3,3]:
            return True  
    
    return False



print(has_33([1, 3, 3]))


"""
The use of abs
"""


# SOLUTION
# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/04-Function%20Practice%20Exercises%20-%20Solutions.ipynb



def almost_there(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))


print(almost_there(80))


"""
 for else statement

 applied when BREAK is there.

 means if it went thru an entire for loop, and it never break, 
 then the else statement is going to execute.
"""

    # x is going through every number up to input num
    while x<= num:
        #Check if x is prime
        for y in range(3,x,2):
            if x%y == 0:
                x+= 2
                break
        else:
            primes.append(x)
            x+= 2



"""
Lambda
"""




"""
map()
map() function returns a map object(which is an iterator) of the results after applying 
the given function to each item of a given iterable (list, tuple etc.)
"""

>>> def square(num):
...     return num**2
...

>>> my_nums= [1,2,3,4,5]
>>> for item in map(square, my_nums):
...     print(item)
...
1
4
9
16
25

>>> list(map(square, my_nums))
[1, 4, 9, 16, 25]


>>> for f in my_nums:
...     result= f**2
...
>>> for f in my_nums:
...     result= f**2
...     print(result)
...
1
4
9
16
25

>>> def splicer(mystring):
...     if len(mystring)%2 == 0:
...             return 'EVEN'
...     else:
...             return mystring[0]
...
>>> names= ['Andy', 'Eve', 'Sally']
>>> list(map(splicer, names))
['EVEN', 'E', 'S']
>>>


"""
filter()
"""


>>> def check_even(num):
...     return num%2 == 0
...
>>> mynums= [1,2,3,4,5,6]


>>> list(filter(check_even,mynums))
[2, 4, 6]

>>> for f in filter(check_even, mynums):
...     print(f)
...
2
4
6

"""
lambda
"""
def square(num): return num**2


print(square(2))
print("@@@@@@@@")


square= lambda num: num**2

print(square(5))
print("@@@@@@@@")


mynums= [1,2,3,4,5]

print( list(map(lambda num: num**2, mynums)) )


print( list(filter(lambda num: num%2 == 0, mynums)) )

print("@@@@@@@@")


names= ['Andy', 'Eve', 'Sally']

print(  list(map(lambda x:x[0], names)) )



"""
Nested statement and scope
"""
    #GLOBAL
>>> name= 'This is a global string'

>>> def greet():
        #ENCLOSING
...     name= 'Sammy'
...     def hello():
...             print('Hello' + name)
...     hello()
...
>>> greet()
HelloSammy


>>> def greet():
        #ENCLOSING
...     #name= 'Sammy'
...     def hello():
...             print('Hello' + name)
...     hello()
...
>>> greet()
HelloThis is a global string



>>> def greet():
        #ENCLOSING
...     name= 'Sammy'
...     def hello():
...             #LOCAL
...             name= 'IM A LOCAL'
...             print('Hello'+ name)
...     hello()
...
>>> greet()
HelloIM A LOCAL


>>> x= 50
>>> def func():
...     global x
...     print(f'X is {x}')
...     #LOCAL REASSIGMENT
...     x= 200
...     print(f'I JUST GLOBALLY CHANGED X TO {x}')
X is 50
I JUST GLOBALLY CHANGED X TO 200

"""
interactive
"""

def user_choice():

	#VARIABLES

	#Initial
	choice= "WRONG"
	acceptable_range= range(0,10)
	within_range= False

	#TW CONDITIONTO CHECK
	#DIGIT OR WITHIN_RANGE== False
	while choice.isdigit() == False or within_range == False:

		choice= input("Please enter a number (0-10): ")

		#DIGIT CHECK
		if choice.isdigit() == False:
			print("sry thast not a digit")

		#RANGE CHECK
		if choice.isdigit() == True:
			if int(choice) in acceptable_range:
				within_range= True
			else:
				print("ur outta 0-10")
				within_range= False	

	return int(choice)


user_choice()


"""
tic tac toe

https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/9442472#content

"""


# smart way to check if full board

def space_check(board, position):

    return board[position] == ''



def full_board_check(board):

    for i in range(1,10):
        #this part man
        if space_check(board, i):
            return False

    #BOARD IS  FULL IF WE RETURN True
    return True


test_board = ['#','X','','','X','','','X','','']

full_board_check(test_board)


# ways of conditional of tic tc toe

def win_check(board, mark):
    
    #these two are the same logic
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[4] == board[5] == board[6] == mark)



# this bit is nice
def replay():

    choice= input("Play again? Enter Yes or No")

    return choice == 'Yes'


"""
class
"""

class Dog():
    
    #CLASS OBJECT ATTRIBUTE
    #SAME FOR ANY INSTANCE OF A CLASS
    #Dont need SELF because SELF is a reference for this particular instance of a class
    species= 'mammal'

    def __init__(self, breed, name):

        #Attributes
        self.breed= breed
        self.name= name

    #OPERATIONS/Actions ---> Methods
    def bark(self, number):
        print(f"WOOF! My name is {self.name} and the number is {number}")




my_dog= Dog('Lab', 'Frankie')

print(my_dog.breed, my_dog.name)
print(my_dog.species)

my_dog.bark(1111)



#another class

class Circle():

    #CLASS OBJECT ATTRIBUTE
    pi= 3.14

    def __init__(self, radius=1):

        self.radius= radius
        # https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/9478294?start=450#content
        #if u hvae atribue it doesnt have to be defined from particular parameter call
        #15:00
        #CLASS OBJECT ATTRIBUTE, you can call by self.pi, Circle.pi  @@@@@@
        self.area= radius*radius*self.pi

    #METHOD
    def get_circumference(self):
        #self.pi, Circle.pi  @@@@@@
        return self.radius * self.pi * 2


my_circle= Circle(30)

print(my_circle.pi)
print(my_circle.radius)
print(my_circle.area)

print(my_circle.get_circumference())



#another class

class Girl():

    h= 222222

    def __init__(self, name):

        self.name= name

        self.age= Girl.h


girls= Girl("koko")
print(girls.age)


"""
INHERITANCE
"""

class Animal():

    def __init__(self):
        print("Animal created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I'm eating")



class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    #OVERRIDE
    def who_am_i(self):
        print("im a dGOGGG")

    #add on methods
    def bark(self):
        print("WOOF!!")



mydog= Dog()

mydog.bark()




class Vehicle():

    def __init__(self, max_speed, mileage):

        self.max_speed= max_speed
        self.mileage= mileage



class Bus(Vehicle):
    def __init__(self, max_speed, mileage):
        Vehicle.__init__(self, max_speed, mileage)



bbb= Bus(9, 1100001)


"""
Polymorph
"""

class Dog:

    def __init__(self, name):
        self.name= name

    def speak(self):
        return self.name + "says woof!"



class Cat():

    def __init__(self, name):
        self.name= name

    def speak(self):
        return self.name + "says meow!"



niko= Dog("niko")
felix= Cat("felix")

print(niko.speak())
print(felix.speak())
print("@@@@@@@@@")


for pet in [niko, felix]:

    print(type(pet))
    print(type(pet.speak()))


"""
Abstract class
"""

#Abstract class, not expected to create instance with it,
#The reason its abstract class is the method dont do anyting, it expect you to override it.


class Animal():

    def __init__(self, name):
        self.name= name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")



myanimal= Animal('fred')

#myanimal.speak()

class Dog(Animal):

    def speak(self):
        return self.name + "says meow!"


fido= Dog("Fido")
print(fido.speak())


"""
Special methods, magic, dunder
"""

class Sample():
    pass



mysample= Sample()

print(mysample)



class Book():

    def __init__(self, title, author, pages):

        self.title= title
        self.author= author
        self.pages= pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object has been deleted@@@@@")
        


b= Book("python book", "Jose", 20)
print(b.__len__())

print(b)

print(len(b))

del b
print(b)

