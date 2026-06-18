class Solution:
    def rotate(self, nums,k):
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0 or not nums:
            return nums

        k = k % len(nums)

        def reverse(arr):
            if not arr :
                return arr
            l = 0
            r = len(arr)-1
            while l<r:
                arr[l],arr[r] = arr[r],arr[l]
                l+=1
                r-=1
            return arr

        nums     = reverse(nums)
        nums[:k] = reverse(nums[:k])
        nums[k:] = reverse(nums[k:])

        return nums
    
s=Solution()

print(s.rotate([1,2,3,4,5,6,7],3))