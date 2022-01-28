import one

print("Top level in TWO.py")

one.func()


if __name__ == '__main__':
	print("TWO.py is being run DIRECTLY")
else:
	print("TWO has been imported!")