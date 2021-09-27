def myfunc(*args, **kwargs):

	print(args)
	print(kwargs)
	print(f"I would like {args[0]} {kwargs['food']}")


myfunc(10,20,30, fruit='orange', food='eggs', animal='dog')


def view(*args, **kwargs):
	

	print(f"{kwargs}")


my_kwargs = dict(hello='world',star='wars')

view(**my_kwargs)

