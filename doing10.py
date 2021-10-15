def up_low(s):
    list_up= []
    list_low= []


    for f in s.split():
    	if f[0].isupper() == True:
    		list_up.append(f)

    	elif f.islower() == True:
    		list_low.append(f)
    		joined= ''.join(f)
    
    ups= len(list_up)		
    lows= len(joined)

    print(f"we got {ups} and {lows}")

    return ups, lows


up_low('Hello Mr. Rogers, how are you this fine Tuesday?')





