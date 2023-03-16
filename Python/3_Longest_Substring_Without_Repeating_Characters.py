
#leetcode ex1
# warnings.filterwarnings('ignore')


class Solution(object):
   def lengthOfLongestSubstring(self, s):
    i =0
    j = 0
    temp={}
    ans = 0
    while j < len(s):
        if s[j] not in temp or i>temp[s[j]]:
            ans = max(ans,(j-i+1))
            temp[s[j]] = j
        else:
            i = temp[s[j]]+1
            ans = max(ans,(j-i+1))
            j-=1
        j+=1
    return ans
def main():
    solution = Solution()
    ans = solution.lengthOfLongestSubstring("pwwkew")
    print("The length of the longest non-repeating character substring is " + str(ans))
if __name__ == "__main__":
    main() 
    
 