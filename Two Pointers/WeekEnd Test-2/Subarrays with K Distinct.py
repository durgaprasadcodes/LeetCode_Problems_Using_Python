import collections
class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        return self.AtmostK(nums,k)- self.AtmostK(nums,k-1)
    def  AtmostK(self,nums,k):
        d=collections.defaultdict(int)
        l=0
        count=0
        for r in range (len(nums)):
            d[nums[r]]+=1
            while len(d)>k:
                d[nums[l]]-=1
                if d[nums[l]]==0:
                    del d[nums[l]]
                l+=1
            count+=(r-l+1)
        return count

        