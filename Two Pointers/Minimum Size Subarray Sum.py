class Solution:
    def minSubArrayLen(self, target ,nums):
        if len(nums)==1:
            return 1 if  nums[0]>=target else 0
        i=0
        cur_len=float('inf')
        cur_sum=0
        for j in range(len(nums)):
            cur_sum+=nums[j]
            while cur_sum >= target:
                cur_len=min(cur_len,j-i+1)
                cur_sum-=nums[i]
                i+=1
        return cur_len if cur_len!=float('inf') else 0
    
                
s=Solution()
print(s.minSubArrayLen(7,[2,3,1,2,4,3]))
print(s.minSubArrayLen(4,[1,4,4]))
print(s.minSubArrayLen(11,[1,1,1,1,1,1,1,1]))