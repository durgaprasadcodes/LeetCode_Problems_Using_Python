class Solution(object):
    def trap(self, nums):
        """
        :type height: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        l,r=0,len(nums)-1
        left_max,right_max=nums[l],nums[r]
        res=0
        while l<r:
            if nums[l]<nums[r]:
                left_max=max(left_max,nums[l])
                res+=left_max-nums[l]
                l+=1
            else:
                right_max=max(right_max,nums[r])
                res+=right_max-nums[r]
                r-=1
        return res
        
s=Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
                
# Time complexity: O(n)
# Space complexity: O(1)