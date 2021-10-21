class User():

	def __init__(self, first_name, last_name, age, looks):

		self.first_name= first_name
		self.last_name= last_name
		self.age= age
		self.looks= looks


	def describe_user(self):
		print(f"he's {self.age} and pretty {self.looks}")

	def greet_user(self):
		print(f"hey {self.first_name}, ur last name {self.last_name} , ur {self.age}")



user1= User("sean", "takei", 22, "handsomeee")

user1.describe_user()
user1.greet_user()