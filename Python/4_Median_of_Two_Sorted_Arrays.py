class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merg = nums1.copy() 
        merg.extend(nums2)
        merg.sort()

        if len(merg)%2!=0:
            return float((merg[len(merg)//2]))
        else:
            a = merg[len(merg)//2-1]
            b = merg[len(merg)//2]
            return float((a+b)/2)