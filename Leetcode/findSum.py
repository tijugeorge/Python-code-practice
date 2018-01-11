#find the sum of two integers represented as strings, return the sum as string, 
#i.e "123" and "456" would return "579".


def findSum(string1, string2):
	if len(string1) > len(string2):
		string1, string2 = string2, string1  #always keep string2 larger
	newString = ''
	print(newString)
	n1, n2 = len(string1), len(string2)

	string1 = string1[::-1]
	string2 = string2[::-1]

	carry = 0
	for i in range(n1):
		summ = (int(string1[i])+int(string2[i])+carry)
		newString += str(summ%10)

		carry = summ//10

	for i in range(n1, n2):
		summ = (int(string2[i])+carry)
		newString += str(summ%10)
		

		carry =summ//10

	if carry:
		newString += str(carry)

	newString = newString[::-1]

	return newString


string1 = '123'
string2 = '19811'

print(findSum(string1, string2))
