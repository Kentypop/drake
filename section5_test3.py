#Use a List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'


for f in st.split():
	for f in f[0]:
		print(f)


#List comprehension is this
mylist= [ f for f in st.split() for f in f[0]]


#A
[word[0] for word in st.split()]

#equivalent of this
for word in st.split():
	word[0]