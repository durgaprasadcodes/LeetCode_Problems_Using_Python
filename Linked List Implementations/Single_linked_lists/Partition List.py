class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head,x):
        if not head :
            return head
        Big_head = ListNode(0)
        Small_head = ListNode(0)
        big = Big_head
        small = Small_head
        curr = head
        while curr:
            if curr.val < x:
                small.next = curr
                small = small.next
            else:
                big.next = curr
                big = big.next
            curr=curr.next
        big.next = None
        small.next = Big_head.next

        return Small_head.next