class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        l=0
        max_len=0
        accept = k 
        no_of_zeros=0
        for r in range(len(nums)):
            no_of_zeros += 1 if nums[r] == 0 else 0

            while no_of_zeros > accept:
                if nums[l] == 0:
                    no_of_zeros-=1
                l+=1
            max_len=max(max_len,r-l+1)
        return max_len
s=Solution()
print(s.longestOnes([1,1,1,0,0,0,1,1,1,1,0],2))

# Time Complexity : O(N)
# Space Complexity : O(1) 