def myfunc(word):
    index= 0 +1
    result= ''

    for f in word:


        if index%2== 0:
            app= f.upper()
            print(app)
            result+= f.upper()
        else:
            app= f.lower()
            result+= app
        index+= 1    

    return print(result)


re= myfunc(word= 'abcdefg')

