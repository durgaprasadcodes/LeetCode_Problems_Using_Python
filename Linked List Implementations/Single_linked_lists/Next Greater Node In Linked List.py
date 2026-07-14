class Solution:
    def nextLargerNodes(self, head):
        curr = head
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next
        ans,stk = [0]*len(arr),[]
        for i  in range(len(arr)):
            while stk and arr[stk[-1]]<arr[i]:
                ans[stk.pop()] = arr[i]
            stk.append(i)
        return ans