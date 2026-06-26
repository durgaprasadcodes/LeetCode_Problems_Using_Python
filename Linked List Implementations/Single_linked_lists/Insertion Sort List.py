class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head):
        
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        curr = head
        while curr:
            prev = dummy
            next_nodes = curr.next
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            curr.next = prev.next
            prev.next = curr
            curr = next_nodes
        return dummy.next
