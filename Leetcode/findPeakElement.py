import math
class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_element = -math.inf
        index = -math.inf
        for i,j in enumerate(nums):
            if j > max_element:
                max_element = j
                index = i


        return index
