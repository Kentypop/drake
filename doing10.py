def paper_doll(text):
	added= ''

	for f in text:
		two_copy = f*3
		added= added+two_copy


	return added


print(paper_doll("Hello"))