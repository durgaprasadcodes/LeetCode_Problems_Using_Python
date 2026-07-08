# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverse(head):
    curr = head
    prev = None
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head = reverse(head)
        cur_max = curr.val
        while curr.next:
            if curr.val >= curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return reverse(head)
