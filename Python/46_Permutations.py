#https://leetcode.com/problems/permutations/
class Solution:
    def permute(nums):
        ans = []
        def subset(p, up):
            if len(up) == 0:
                ans.append(p)
                return 
            ch = up[0]
            for i in range(len(p) + 1):
                subset(p[0:i] + [ch] + p[i:], up[1:])
        subset([], nums)
        return ans

def main():
    solution = Solution
    ans = solution.permute([1,2,3])
    print(ans)

if __name__ == "__main__":
    main()