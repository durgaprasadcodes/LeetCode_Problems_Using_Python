class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeZeroSumSublists(self, head):

        dummy = ListNode(0,head)
        prefix = 0
        curr = dummy
        seen = {}
        while curr:
            prefix += curr.val
            seen[prefix] = curr
            curr = curr.next

        prefix = 0                
        curr = dummy
        while curr:
            prefix += curr.val
            curr.next = seen[prefix].next
            curr = curr.next
        return dummy.next