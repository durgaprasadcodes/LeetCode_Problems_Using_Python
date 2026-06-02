class Solution(object):
    def runningSum(self, nums):
        s=0
        for i in range(len(nums)):
            nums[i]+=s
            s=nums[i]
        return nums
s=Solution()
print(s.runningSum([1,2,3,4]))
