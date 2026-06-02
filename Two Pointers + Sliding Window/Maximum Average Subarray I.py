class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if len(nums)==1:
            return float(nums[0])
        if len(nums)==k:
            return sum(nums)/float(k)
        if k==1:
            return float(max(nums))
        
        actual_sum=curr_sum=sum(nums[:k])
        j=0
        for i in range(k,len(nums)):
            curr_sum=curr_sum-nums[j]+nums[i]
            if curr_sum>actual_sum:
                actual_sum=curr_sum
            j+=1
        return actual_sum/float(k)
        

s=Solution()
print(s.findMaxAverage([0,4,0,3,2],1))