class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        s = nums.count(val)
        
        for i in range(s):
            nums.remove(val)
        
        return len(nums)