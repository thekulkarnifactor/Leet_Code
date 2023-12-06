class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        seven_days = n/7
        remaining_days = n%7
        count = 0
        monday = 0
        for i in range(1, int(seven_days+1)):
            monday = i
            for i in range(monday, monday+7):
                count += i                
        for i in range(monday+1, monday+remaining_days+1):
            count+= i
        return count
def main():
    solution = Solution()
    ans = solution.totalMoney(20)
    print(ans)
if __name__ == "__main__":
    main() 
        
        