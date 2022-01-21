work_hours = [('Abby',100),('Billy',800),('Cassie',400)]


def emp_month(aa):

	maxine= 0
	best= ''

	for emp, hours in aa:
		#add maxine if max
		if hours > maxine:
			maxine= hours
			best= emp

	return maxine, best




print(emp_month(work_hours))

onee, twoo= emp_month(work_hours)
print(onee)
print(twoo)