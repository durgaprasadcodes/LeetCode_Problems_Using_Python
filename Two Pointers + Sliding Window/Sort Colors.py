class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low=0
        cur=0
        high=len(nums)-1
        while cur<=high:
            if nums[cur]==0:
                nums[low],nums[cur]=nums[cur],nums[low]
                low+=1
                cur+=1
            elif nums[cur]==1:
                cur+=1
            else:
                nums[high],nums[cur]=nums[cur],nums[high]
                high-=1
        return nums
s=Solution()
print(s.sortColors([2,0,2,1,1,0]))

# Time Complexity O(n) - Dutch National Flag Algorithm
# Space Complexity O(1)