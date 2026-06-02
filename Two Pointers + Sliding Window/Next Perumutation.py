class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1:
            return nums

        def reverse (nums,idx):
            l,r=idx,len(nums)-1
            while l<=r:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
            return nums

        pivot_idx=-1
        

        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                pivot_idx = i
                break

        if pivot_idx == -1:
            return reverse(nums,0)

        for j in range(len(nums)-1,pivot_idx,-1):
            if nums[j]>nums[pivot_idx]:
                swapp=j
                break
        
        nums[pivot_idx],nums[swapp] = nums[swapp],nums[pivot_idx]
        
        return reverse(nums,pivot_idx+1)
    
s=Solution()
print(s.nextPermutation([1,2,3]))

# Time Complexity O(N)
# Space Complexity O(1)