# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow=fast=head
        c=0
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow == fast :
                c=1
                break
        if c:
            res=head
            while slow!=res:
                slow=slow.next
                res=res.next
            return slow
        return None
