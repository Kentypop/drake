work_hours = [('Abby',100),('Billy',400),('Cassie',800)]


def best_emp(work_hours):
	mylist= []

	for name, hours in work_hours:
		#Get the max 
		mylist.append(hours)
		max_hours= max(mylist)
		

	return max_hours



aa= best_emp(work_hours)		

print(aa)
