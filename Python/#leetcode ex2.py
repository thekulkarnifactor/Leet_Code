#https://leetcode.com/problems/zigzag-conversion/

from ast import main


class Solution(object):
    def convert(self, string_s, numRows):
        string_s = string_s.upper()
        if numRows == 1:
            return string_s
        else:
            ans = ""
            for i in range(numRows):
                if i == 0 or i == numRows - 1:
                    for j in range(len(string_s)):
                        if j % (numRows - 1) == 0:
                            ans += string_s[j]
                else:
                    for j in range(len(string_s)):
                        if j % (numRows - 1) == 0:
                            ans += string_s[j]
                        elif j % (numRows - 1) == i:
                            ans += string_s[j]
            return ans

def main():
    solution = Solution()
    print(solution.convert("PAYPALISHIRING", 3))

if __name__ == "__main__":
    main()