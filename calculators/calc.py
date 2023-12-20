''' My first calculator'''



print ("Hello, its calculator\n")

def calc():
	while True:
		try:
			num = int(input("How much operations do you want continue in line (5 max)?: "))
			if num <= 5:
				break
		except:
				print ("Enter only number of operations\n")
	if num == 1:
		q = int(input("Enter first number: "))
		s1 = input("Enter sign: ")
		w = int(input("Enter second number: "))	
		if s1 == "+":
			print ('{} + {} = '.format(q, w))
			print (float(q + w))
		elif s1 == "-":
			print ('{} - {} = '.format(q, w))
			print (float(q - w))
		elif s1 == "*":
			print ('{} * {} = '.format(q, w))
			print (float(q * w))
		elif s1 == "/":
			print ('{} / {} = '.format(q, w))
			print (float(q / w))
		else:
			print ("Enter only +, -, *, /")
	elif num == 2:
		q = int(input("Enter first number: "))
		s1 = input("Enter sign: ")
		w = int(input("Enter second number: "))	
		s2 = input("Enter sign: ")
		e = int(input("Enter third number: "))	
		print (float(q) + int(s1) + float(w) + int(s2) + float(e))
	elif num == 3:
		q = int(input("Enter first number: "))
		s1 = input("Enter sign: ")
		w = int(input("Enter second number: "))	
		s2 = input("Enter sign: ")
		e = int(input("Enter third number: "))	
		s3 = input("Enter sign: ")
		r = int(input("Enter fourth number: "))	
	elif num == 4:
		q = int(input("Enter first number: "))
		s1= input("Enter sign: ")
		w = int(input("Enter second number: "))	
		s2 = input("Enter sign: ")
		e = int(input("Enter third number: "))	
		s3 = input("Enter sign: ")
		r = int(input("Enter fourth number: "))	
		s4 = input("Enter sign: ")
		t = int(input("Enter five number: "))	
	elif num == 5:
		q = int(input("Enter first number: "))
		s1 = input("Enter sign: ")
		w = int(input("Enter second number: "))	
		s2 = input("Enter sign: ")
		e = int(input("Enter third number: "))	
		s3 = input("Enter sign: ")
		r = int(input("Enter fourth number: "))	
		s4 = input("Enter sign: ")
		t = int(input("Enter five number: "))	
		s5 = input("Enter sign: ")
		y = int(input("Enter six number: "))	
	else:
		print ("Maximum is 5 operation")
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





