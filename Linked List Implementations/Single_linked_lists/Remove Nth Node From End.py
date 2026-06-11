# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head):
        if not head:
            return None
            
        dummy = ListNode(0,head)
        f=s=dummy
        for _ in range(n):
            f=f.next
        
        while f and f.next:
            f=f.next
            s=s.next

        s.next=s.next.next
        return dummy.next

        

        
        