#13_Roman_to_Integer
class Solution(object):
    def constraints(self, s):
        flag = False
        #1 <= s.length <= 15
        if len(s) <= 15 and len(s) >= 1:
            # print("1st Pass")
            # s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M')
            roman_list = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
            if all(letter in roman_list for letter in s):
                # print("2nd Pass")
                flag = True
            else:
                flag = False
        else:
            flag = False
        return flag

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # print("Constraints check")
        # set numbers
        roman_data = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        int_val = 0
        if self.constraints(s):
            for i in range(len(s)):
                if i+1<len(s) and s[i] == 'I' and (s[i+1] == 'V' or s[i+1]=='X'):
                    int_val-=roman_data[s[i]]
                elif i+1<len(s) and s[i] == 'X' and (s[i+1] == 'L' or s[i+1]=='C'):
                    int_val-=roman_data[s[i]]
                elif i+1<len(s) and s[i] == 'C' and (s[i+1] == 'D' or s[i+1]=='M'):
                    int_val-=roman_data[s[i]]
                else:
                    int_val += roman_data[s[i]]
        return int_val
def main():
    solution = Solution()
    ans = solution.romanToInt("MCMXCIV")
    # print(ans)
if __name__ == "__main__":
    main()