#Minimize the maximum difference between the heights

def getMinDiff(arr, n, k):
	#there should be atleast 2 elements
	if n<=1:
		return 0

	#sort array in increasing order
	arr.sort()

	#initialize maximum and minimum
	maxi = arr[n-1]
	mini = arr[0] 

	#If k is more than difference between maximum 
	#and minimum, add/subtract k to all elements
	#as k cannot decrease the difference
	if (k>=(maxi-mini)):
		for i in range(n):
			arr[i]+=k #subtract would also work
		return maxi-mini

	#In sorted array, first element is minimum
	#and last is maximum, we must add k to minium
	#and subtract k from maximum
	arr[0]+=k
	arr[n-1]-=k

	#Initialize mac and min of modified array (only
	#two elements have been finalized)   
	new_max = max(arr[0], arr[n-1])
	new_min = min(arr[0], arr[n-1])

	#finalize middle n-2 elements
	for j in range(n-1):
		# If current element is less than min of
		# modified array, add k.
		if arr[j]<new_min:
			arr[j]+=k
		#If current element is more than max of
		#modified array, subtract k.
		elif arr[j]>new_max:
			arr[j]-=k
		#arr[j] is between new_min and new_max

		#If arr[j] is closer to new_max, subtract k	
		elif ((arr[j] - new_min) > (new_max - arr[j])):
			arr[j]-=k
		#Else add k
		else:
			arr[j]+=k

		#Update new_max and new_min if required  
		new_max = max(arr[j], new_max)
		new_min = min(arr[j], new_min)                   

	#Returns difference between new_max and new_min
	return (new_max-new_min)

#Driver function to test the above function
arr = [1,15,10]
n = len(arr)
k = 6
res = getMinDiff(arr, n, k)

print "Modified array is \n"
for i in range(n):
	print arr[i]

print "Maximum difference is ", res
