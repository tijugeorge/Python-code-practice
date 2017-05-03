#Search an element in a sorted and rotated array
def findNumber(list, x, start, end):
	if start>end:
		return -1
	mid=(start+end)/2
	if list[mid]==x:
		return mid

	if list[start]<list[mid]:
		if x>=list[start] and x<=list[mid-1]:
			return findNumber(list, x, start, mid-1)
		else:
			return findNumber(list, x, mid+1, end)

	else:
		if x>=list[mid] and x<=list[end]:
			return findNumber(list, x, mid+1, end)
		else:
			return findNumber(list, x, start, mid-1)

list = [4,5,6,7,8,9,1,2,3]
print "Your Array is: ", list
x = input("Enter the number you looking for in the array: ")
result = findNumber(list, x, 0, len(list)-1)
print "The positoin of the number you looking for is at %dth position" %(result+1)
