from collections import Counter

mylist= "aaabbccccc"

c= Counter(mylist)

print(c)
print(type(c))

print(list(c))

print(type(list(c)))