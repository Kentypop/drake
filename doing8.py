def simple_gen():
	for x in range(3):
		yield x


for number in simple_gen():
	print(number)


g= simple_gen()

print(next(g))
print(next(g))
print(next(g))