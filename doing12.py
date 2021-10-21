class Girl():

	h= 222222

	def __init__(self, name):

		self.name= name

		self.age= Girl.h


girls= Girl("koko")
print(girls.age)