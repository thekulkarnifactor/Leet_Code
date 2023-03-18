class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        index = -1
        maxlength = 0
        # looping over the string for substrings
        for i in range(length):
            for j in range(i, length):
                ispalindrome = 1
                # checking if string is a palindrome
                for k in range(0, ((j - i) // 2) + 1):
                    if s[i + k] != s[j - k]:
                        ispalindrome = 0
                # if the string is palindrome update maximum length 
                if ispalindrome != 0 and j - i + 1 > maxlength:
                    index = i
                    maxlength = j - i + 1
        # return the substring from updated index till length maxlength
        return s[index:index + maxlength]
def main():
    solution = Solution()
    strings = "ibvjkmpyzsifuxcabqqpahjdeuzaybqsrsmbfplxycsafogotliyvhxjtkrbzqxlyfwujzhkdafhebvsdhkkdbhlhmaoxmbkqiwiusngkbdhlvxdyvnjrzvxmukvdfobzlmvnbnilnsyrgoygfdzjlymhprcpxsnxpcafctikxxybcusgjwmfklkffehbvlhvxfiddznwumxosomfbgxoruoqrhezgsgidgcfzbtdftjxeahriirqgxbhicoxavquhbkaomrroghdnfkknyigsluqebaqrtcwgmlnvmxoagisdmsokeznjsnwpxygjjptvyjjkbmkxvlivinmpnpxgmmorkasebngirckqcawgevljplkkgextudqaodwqmfljljhrujoerycoojwwgtklypicgkyaboqjfivbeqdlonxeidgxsyzugkntoevwfuxovazcyayvwbcqswzhytlmtmrtwpikgacnpkbwgfmpavzyjoxughwhvlsxsgttbcyrlkaarngeoaldsdtjncivhcfsaohmdhgbwkuemcembmlwbwquxfaiukoqvzmgoeppieztdacvwngbkcxknbytvztodbfnjhbtwpjlzuajnlzfmmujhcggpdcwdquutdiubgcvnxvgspmfumeqrofewynizvynavjzkbpkuxxvkjujectdyfwygnfsukvzflcuxxzvxzravzznpxttduajhbsyiywpqunnarabcroljwcbdydagachbobkcvudkoddldaucwruobfylfhyvjuynjrosxczgjwudpxaqwnboxgxybnngxxhibesiaxkicinikzzmonftqkcudlzfzutplbycejmkpxcygsafzkgudy"
    ans = solution.longestPalindrome(strings)
    print(ans)
if __name__ == "__main__":
    main() 
    