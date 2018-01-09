class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dicti = {}
        for i in nums:
            if i in dicti:
                dicti[i] += 1
                return True
            else:
                dicti[i] = 1
        return False
