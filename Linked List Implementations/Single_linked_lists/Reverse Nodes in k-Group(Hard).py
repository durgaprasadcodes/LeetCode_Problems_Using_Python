# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        length = 0
        curr = head
        while curr:
            length+=1
            curr = curr.next

        if length < k:
            return head

        dummy = ListNode(0,head)
        prev  = dummy
        curr = head

        def reverse(head,k):
            curr = head
            prev = None
            
            while k:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                k-=1
            return prev , curr

        for _ in range(int(length//k)):
            cur_head,next_node = reverse(curr,k)

            prev.next = cur_head
            curr.next = next_node

            prev = curr
            curr = next_node

        return dummy.next 

