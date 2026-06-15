class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head ,left ,right):
        if not head or left == right:
            return head

        dummy = ListNode(0,head)
        left_node_prev = dummy

        for _ in range(left - 1):
            left_node_prev = left_node_prev.next

        curr = left_node = left_node_prev.next
        prev = None
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        left_node_prev.next = prev
        left_node.next = curr

        return dummy.next
        
        