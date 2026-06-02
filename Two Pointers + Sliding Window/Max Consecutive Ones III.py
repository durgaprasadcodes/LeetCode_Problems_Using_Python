class Solution(object):
    def longestOnes(self, nums, k):
        i=j=0
        zeros=0
        max_len=0
        while j<len(nums):
            if nums[j]==0:
                zeros+=1
            while zeros>k:
                if nums[i]==0:
                    zeros-=1
                i+=1
            max_len=max(max_len,j-i+1)
            j+=1
        
        return max_len

s=Solution()
print(s.longestOnes([1,1,1,0,0,0,1,1,1,1,0],3))

# Time Complexity: O(n)
# Space Complexity: O(1)