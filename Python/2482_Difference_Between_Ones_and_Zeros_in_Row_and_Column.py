#Python3
class Solution(object):
    def onesMinusZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        def summation(nums) : 
            return 2 * sum(nums) - len(nums)
        m, n = len(grid), len(grid[0])
            
        rows = list(map(summation, grid))
        cols = list(map(summation, zip(*grid)))
        
        for i,j in product(range(m), range(n)):
            grid[i][j] = rows[i] + cols[j]
        return grid