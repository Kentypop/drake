import doing2
import doing3
import doing4

# doing2.py
work_hours = [('Abby',100),('Billy',400),('Cassie',800), ('drake', 1)]


result= doing2.employee_check(work_hours)	
print(result)


# Tuple unpacking with a function call.
name, hours= doing2.employee_check(work_hours)
print(name, hours)



# doing3.py
num= [1,2,3,4,5,6]
print(doing3.check_even(num))    


# doing4.py

print(doing4.add_func(1,2))