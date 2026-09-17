class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        balance= 0
        idx = nums.index(k)
        count = {}
        ans = 0
        for i in range(idx,len(nums)):
            if nums[i]>k:
                balance +=1
            elif nums[i]<k:
                balance -=1
            count[balance] = count.get(balance,0)+1
        balance = 0
        for i in range(idx,-1,-1):
            if nums[i]>k:
                balance +=1
            elif nums[i]<k:
                balance -=1
            ans += count.get(-balance,0)+count.get(1-balance,0)
        return ans
        
            
            