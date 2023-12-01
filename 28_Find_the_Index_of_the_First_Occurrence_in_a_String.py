# class Solution(object):
def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if needle in haystack:
            return haystack.index(needle)
    return -1


haystack = "leetcode"
needle = "code"
print(strStr(haystack, needle))