def sumExceptSelf(nums):
	p = 0
	n = len(nums)
	output = []
	for i in range(0, n):
		output.append(p)
		p = p + nums[i]
	p = 0
	for i in range(n-1, -1, -1):
		output[i] = output[i]+p
		p = p + nums[i]
	return output

nums = [2,3,5,6]
print(sumExceptSelf(nums))
