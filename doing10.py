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
	def bark(self):
		print("WOOF!")



my_dog= Dog('Lab', 'Frankie')


print(type(my_dog))
print(my_dog.breed, my_dog.name)
print(my_dog.species)

my_dog.bark()