# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy= ListNode(0)
        dummy.next=head

        s=f=dummy

        while n:
            f=f.next
            n-=1
        
        while f and f.next:
            s=s.next
            f=f.next
        s.next=s.next.next
        return dummy.next

        

        
        