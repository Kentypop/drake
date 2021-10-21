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