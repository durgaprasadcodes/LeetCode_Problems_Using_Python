class Solution:
    def countMajoritySubarrays(self, nums, target: int) -> int:
        ans = 0
        for i in range(len(nums)):
            count = 0
            for j in range(i,len(nums)):
                count+=1 if nums[j] ==  target else -1
                if count>0:
                    ans += 1
        return ans 
            