# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        curr = head
        prev = None

        while curr:
            Next = curr.next
            curr.next = prev
            prev = curr
            curr = Next
        return prev
    
# Time Complexity O(N)
# Space Complexity O(1)