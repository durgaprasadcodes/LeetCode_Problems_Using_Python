class Solution:
    def numComponents(self, head,nums):
        s = set(nums)
        curr = head
        ans = 0
        while curr:
            if curr.val in s and( not curr.next or curr.next.val not in s ):
                ans+=1
            curr = curr.next
        return ans


