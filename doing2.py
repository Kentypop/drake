work_hours = [('Abby',100),('Billy',400),('Cassie',800), ('drake', 1)]


def employee_check(work_hours):

	current_max= 0
	employee_of_month= ''

	for employee, hours in work_hours:
		#Assign to current max so then you have something to compared
		if hours> current_max:
			current_max= hours 
			employee_of_month= employee
		else:
			pass	

	return (employee_of_month, current_max)		

