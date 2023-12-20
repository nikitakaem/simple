
def calc():
	calc = input("Type calculation:\n")

	print("Answer: " + str(eval(calc)))
	again()
	
def again():
	clagain = input ("Do you want calculate again?(Y/N): ")
	if clagain.upper() == "Y":
		calc()
	elif clagain.upper() == "N":
		print ("See you later!")
		quit()
	else:
		again()
calc()


