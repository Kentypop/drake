def hello(name="Jose"):
	print("the hello() function has been executed!")

	def greet():
		return '\t This is the greet() func inside hello!'

	def welcome():
		return '\t This is welcome() inside hello'

	print("Im going to return a function!")

	if name == 'Jose':
		return greet
	else:
		return welcome



my_new_func= hello('Jose')

print(my_new_func)
print(my_new_func())