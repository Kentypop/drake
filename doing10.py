def user_choice():

	#VARIABLES

	#Initial
	choice= "WRONG"
	acceptable_range= range(0,10)
	within_range= False

	#TW CONDITIONTO CHECK
	#DIGIT OR WITHIN_RANGE== False
	while choice.isdigit() == False or within_range == False:

		choice= input("Please enter a number (0-10): ")

		#DIGIT CHECK
		if choice.isdigit() == False:
			print("sry thast not a digit")

		#RANGE CHECK
		if choice.isdigit() == True:
			if int(choice) in acceptable_range:
				within_range= True
			else:
				print("ur outta 0-10")
				within_range= False	

	return int(choice)


user_choice()