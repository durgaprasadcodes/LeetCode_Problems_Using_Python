class Solution(object):
    def pivotArray(self, nums, pivot):
        res=[pivot]*nums.count(pivot)
        res1=[i for i in nums if i<pivot]
        res2=[i for i in nums if i>pivot]
        return res1+res+res2
        
s=Solution()
print(s.pivotArray([9,12,5,10,14,3,10],10))