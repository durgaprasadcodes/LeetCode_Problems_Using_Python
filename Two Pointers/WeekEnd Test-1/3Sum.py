class Solution(object):
    def threeSum(self, nums):
        if len(nums)<3:
            return []
        if len(nums)==3 and sum(nums)==0:
            return [nums]
        nums.sort()
        res=set()
        for i in range(len(nums)-2):
            if nums[i]==nums[i-1] :
                continue
            r=i+1
            l=len(nums)-1
            while r<l:
                s=nums[i]+nums[r]+nums[l]
                if s == 0:
                    res.add((nums[i],nums[r],nums[l]))
                if s > 0:
                    l-=1
                else:
                    r+=1
        return [list(i) for i in res]