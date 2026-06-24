# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head,k):
        if not k:
            return []

        curr = head
        length = 0
        while curr:
            curr = curr.next
            length+=1

        res = []
        curr = head
        Base_size = length // k
        Extra_nodes = length % k
        
        for i  in range(k):
            res.append(curr)
            for j in range( Base_size -1 + (1 if Extra_nodes else 0)):
                if not curr: break
                curr = curr.next
            Extra_nodes -= 1 if Extra_nodes > 0 else 0
            if curr :
                curr.next , curr = None , curr.next
        return res