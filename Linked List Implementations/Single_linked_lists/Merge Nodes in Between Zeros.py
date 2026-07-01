class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_sum = 0
        dummy = ListNode(-1)
        prev = dummy
        curr = head.next
        while curr:
            if curr.val == 0:
                curr.val = curr_sum
                prev.next = curr
                prev = prev.next
                curr_sum = 0
            else:
                curr_sum += curr.val
            curr = curr.next
        head  = dummy.next
        return dummy.next