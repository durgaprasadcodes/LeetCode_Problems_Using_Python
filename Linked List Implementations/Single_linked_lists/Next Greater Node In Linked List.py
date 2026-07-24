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
        return ans# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head):
        
        curr = head
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next
        res = [0]*len(arr)
        stack = []
        for i in range(len(arr)):
            while stack and arr[stack[-1]]<arr[i]:
                idx = stack.pop()
                res[idx] = arr[i]
            stack.append(i)
            
        return res