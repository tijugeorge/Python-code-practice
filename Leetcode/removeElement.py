    def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        print(len(nums))
        while i < len(nums):
            if nums[i] != val:
                i+=1
            else:
                nums.pop(i)
        return len(nums)
