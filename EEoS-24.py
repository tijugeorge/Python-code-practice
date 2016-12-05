
import decimal
print "How many of you guys joining the plan"
People_count= float(input("Please enter a number: "))
def isWhole(x):
	if(x%1 == 0):
		return True
	else:
		print False

while True:
		#try:
		#People_count= float(input("Please enter a number: "))
		#not float(People_count).is_integer()
		#if People_count.isdigit():
		#except Exception ,e:
        #print "Program halted incorrect data entered",type(e)
		#if (People_count < 1 and People_count > 0) or People_count <0:
		#	print "Enter a valid people count! "
		print "Enter a number and i\'ll tell\nyou if its whole or not:"
		if(People_count= isWhole(float(raw_input('Your number please: ')))):
			print 'Well, this is clearly a whole number.'
		else:
			print 'Ick, I dont like decimal numbers'

		if People_count == 1:
			print "Your monthly payment is $40"
		elif People_count == 2:
			print "Your monthly payment is $40+$30=$70"
			print "Each person will pay $", (40+30)/2
		elif People_count == 3:
			print "Your monthly payment is $40+$30+$20=$90"
			print "Each person will pay $", (40+30+20)/3
		elif People_count == 4:
			print "Your monthly payment is $40+$30+$20+$10=$100"
			print "Each person will pay $", (40+30+20+10)/4
		elif People_count == 5:
			print "Your monthly payment is $40+$30+$20+$10+free=$100"
			print "Each person will pay $", (40+30+20+10+0)/5
		else:
			print "Well taking %s people or more is not possible with any existing plans" %People_count
			break
	
			