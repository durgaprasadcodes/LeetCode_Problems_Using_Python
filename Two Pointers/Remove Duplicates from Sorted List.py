# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        if head == None:
            return head
        prev=head
        curr=head.next

        while curr:
            if prev.val != curr.val :
                prev.next = curr
                prev=curr
            curr=curr.next
        prev.next = None

        return head
    
# Time Complexity: O(n)
# Space Complexity: O(1)