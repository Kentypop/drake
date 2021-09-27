# https://www.udemy.com/course/complete-python-bootcamp/learn/quiz/4397024#notes
# https://www.udemy.com/course/complete-python-bootcamp/learn/quiz/4397024#notes

def myfunc(word):
    result = ""
    index = 0
    for letter in word:
        if index % 2 == 0:
            result += letter.lower()
        else:
            result += letter.upper()
        index += 1
        print(index)
        print("@@@@@")

    return print(result)


myfunc("abcdefg")    



#BETTER with enumerate
def myfunc(word):
    result = ""
    for index, letter in enumerate(word):
        if index % 2 == 0:
            result += letter.lower()
        else:
            result += letter.upper()
    return result



re= myfunc("abcdefg")
print(re) 