#Search, insert and delete in an unsorted array
#Search Operation

def findElement(arr, n, key):
	for i in range(n):
		if arr[i] == key:
			return i
	return -1

#driver program
arr = [12, 34, 10, 6, 40]
n = len(arr)
key = 40
position = findElement(arr, n, key)

if position==-1:
	print "Element not found"
else:
	print "Element found at position: %r" %(str(position+1))

	
#Insert Operation

#Inserts a key in arr[] of given capacity.  n is current
# size of arr[]. This function returns n+1 if insertion
# is successful, else n.

def insertSorted(arr, n, key, capacity):
	"""cannot insert more elements if n is already 
	more than or equal to capacity"""
	if n>=capacity:
		return n
	arr[n] = key
	return n+1

#driver program
arr = [12, 16, 20, 40, 50, 70]
capacity = len(arr)
n = 5
key = 26

print "Before insertion: "

for i in range(n):
	print "%r" %arr[i]

#inserting key
n = insertSorted(arr, n, key, capacity)

print "\nAfter insertion: "

for i in range(n):
	print "%r" %arr[i]
	


#Delete Operation
#in delete operation, the element to be deleted is searched 
#using the linear search and then delete operation is performed followed by shifting the elements.

#To search a key to be deleted
#findElement(arr, n, key)

#function to delete an element
def deleteElement(arr, n, key):
	pos = findElement(arr, n, key)
	if pos==-1:
		print "Element not found"
		return n

	#deleting element
	for i in range(pos, n-1, 1):
		arr[i] = arr[i+1]
	return n-1

#Function to implement search operation
def findElement(arr, n, key):
	for i in range(n):
		if arr[i] == key:
			return i
	return -1

#driver code
arr = [10, 50, 30, 40, 20]
n = len(arr)
key = 30
print "Array before deletion\n"
for i in range(n):
	print "%r"%arr[i]
n = deleteElement(arr, n, key)

print "\n\nArray after deletion\n"
for i in range(n):
	print "%r"%arr[i]
