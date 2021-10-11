st = 'Print every word in this sentence that has an even number of letters'

for f in st.split():
	if len(f)%2 == 0:
		print(f"{f} is even!")