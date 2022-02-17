import re


text= "my phone once, my phone twice"

pattern= "phone"

match= re.findall(pattern, text)

print(match)


for match in re.finditer("phone", text):
	print(match)


