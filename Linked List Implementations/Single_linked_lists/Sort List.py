class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head

        prev = None
        rightHead = f = head
        while f and f.next:
            prev = rightHead
            rightHead = rightHead.next
            f = f.next.next

        prev.next = None

        left = self.sortList(head)
        right = self.sortList(rightHead)

        dummy = ListNode(0)
        tail = dummy
        
        while left and right :
            if  left.val < right.val:
                tail.next = left
                left = left.next
            else :
                tail.next = right
                right = right.next
            tail = tail.next
        tail.next = left if left else right 

        return dummy.next


