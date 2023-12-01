# class Solution(object):
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    count=0
    sign=1
    if x<0:
        sign=-1
        x=x*-1
    while x>0:
        rem=x%10
        count=count*10+rem
        x=x//10
    if not -2147483648<count<2147483647:
        return 0
    return sign*count


    
x = -123
print(reverse(x))