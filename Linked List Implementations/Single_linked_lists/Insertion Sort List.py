class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode(0,head)
        curr = head.next
        tail = head
        while curr:
            nxt_nodes = curr.next
            if tail.val<=curr.val:
                tail = curr
                curr = nxt_nodes
                continue
            tail.next = curr.next
            prev = dummy
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            curr.next = prev.next
            prev.next = curr
            curr = nxt_nodes
        return dummy.next