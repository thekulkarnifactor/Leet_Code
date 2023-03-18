#https://leetcode.com/problems/zigzag-conversion/
class Solution(object):
    def convert(self, s, numRows):
        s = s.upper()
        if numRows == 1: return s

        res = ""
        for r in range(numRows):
            increment = 2 * (numRows - 1)
            for i in range(r, len(s), increment):
                print("i: ", i)
                print("adding: ", s[i])
                res += s[i]
                if(r > 0 and r < numRows - 1 and
                   i + increment - 2 * r < len(s)):
                    print("formaula: ",i + increment - 2 * r)
                    print("adding: ", s[i + increment - 2 * r])
                    res += s[i + increment - 2 * r]
        return res
def main():
    solution = Solution()
    print(solution.convert("PAYPAL", 3))

if __name__ == "__main__":
    main()