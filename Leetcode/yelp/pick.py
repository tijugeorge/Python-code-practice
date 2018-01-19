import random
class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        arr = []
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                arr.append(i)
        return random.choice(arr)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
