class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        result = '' 
        count = 1
        for i in range(1, len(num)):
            if num[i] == num[i-1]:
                count+=1
            else:
                count = 1
            if count == 3:
                result = max(result, num[i] * 3)
                
        return result

def main():
    solution = Solution()
    ans = solution.largestGoodInteger("6777133339")
    print(ans)
if __name__ == "__main__":
    main() 