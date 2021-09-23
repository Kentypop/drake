#Go through the string below and if the length of a word is even print "even!"

st = 'Print every word in this sentence that has an even number of letters'


for f in st.split():
	num= len(f)

	if num%2 == 0 :
		print(f"This {f} is even")
	else:
		print(f"This {f} is booo")	
