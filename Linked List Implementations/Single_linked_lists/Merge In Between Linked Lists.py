class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        dummy = ListNode(0,list1)
        left_attachment = dummy

        for _ in range(a):
            left_attachment = left_attachment.next
        right_attachment = left_attachment.next

        for _ in range(b-a+1):
            right_attachment = right_attachment.next
        list2_end = list2

        while list2_end and list2_end.next:
            list2_end = list2_end.next

        left_attachment.next = list2
        list2_end.next = right_attachment

        return dummy.next
    

# Complexity	Value
# ----------    ----- 
# Time	        O(n + m)
# Space	        O(1)