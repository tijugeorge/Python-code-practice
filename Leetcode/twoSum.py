nums = [3,2,4,1,5]
target = 6

class Solution(object):
    def twoSum(self, nums, target):
        check = {}
        for i,num in enumerate(nums):
            if num not in check:
                check[target-num]=i
                print "check and i is given as: ",check, i
            else:
                return [check[num],i]

ss = Solution()
y = ss.twoSum(nums, target)
print y

#Optimized from o(n^2) to O(n)

def twoSum(nums, target):
	for i in range(len(nums)):
		for j in range(len(nums)):
			if i==j:
				pass
			elif nums[i]+nums[j]==target:
				return [i, j]
print twoSum(nums, target)
