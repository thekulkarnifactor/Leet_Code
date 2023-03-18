#leetcode ex3 
# remove Nth From End
class Solution:
    def removeNthFromEnd(self, head, n: int):
        length = 0
        current = head
        while current is not None:
            current = current.next
            length += 1
            
        if length == 1 and n == 1:
            return None
        elif length == n:
            return head.next
        
        n = length - n - 1
        current = head
        
        while n > 0:
            current = current.next
            n -= 1
            
        if current.next.next is None:
            current.next = None
        else:
            target = current.next
            current.next = target.next
            del target
            
        
        return head