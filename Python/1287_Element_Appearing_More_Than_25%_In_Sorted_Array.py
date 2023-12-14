#Python 3
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        ans=len(arr)//4
        for i in set(arr):
            if arr.count(i)>ans:
                return i