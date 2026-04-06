class Solution(object):
    def findUnsortedSubarray(self, nums):
        n=len(nums)
        l,r=0,n-1
        if(n<=1):
            return 0
        while(l<n-1 and nums[l]<=nums[l+1]):
            l+=1
            if l==n-1:
                return 0
        while(r>0 and nums[r]>=nums[r-1]):
            r-=1
        minVal=min(nums[l:r+1])
        maxVal=max(nums[l:r+1])
        while(l>0 and minVal<nums[l-1]):
            l-=1
        while(r<n-1 and maxVal>nums[r+1]):
            r+=1
        return r-l+1
s=Solution()
print(s.findUnsortedSubarray([2,6,4,8,10,9,15]))

# Time Complexity: O(n)
# Space Complexity: O(1)