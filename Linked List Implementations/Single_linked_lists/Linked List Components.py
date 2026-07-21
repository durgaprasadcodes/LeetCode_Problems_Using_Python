class Solution:
    def numComponents(self, head,nums):

        s = set(nums)
        res = count = 0
        prev = None
        curr = head
        while curr:
            if curr.val in s:
                count+=1
            elif count!=0:
                res+=1
                count = 0
            prev = curr
            curr = curr.next

        return res+(1 if prev.val in s else 0)