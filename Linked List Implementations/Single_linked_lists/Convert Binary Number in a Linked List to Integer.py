class Solution:
    def getDecimalValue(self, head) -> int:
        if not head or not head.next:
            return head.val

        curr = head
        res = 0
        
        while curr:
            res = res*2 + curr.val
            curr = curr.next
        
        return res