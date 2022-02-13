import re


text= "My phone number is 408-555-1234"

#phone= re.search("408-555-1234", text)

phone= re.search(r"\d{3}-\d{3}-\d{4}", text)

print(phone)

print(phone.group())