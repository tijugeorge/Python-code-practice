class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, j in enumerate(nums):
            if (target - j) in nums and nums.index(target-j)!=i:
                t = target - j
                return [i, nums.index(t)]
