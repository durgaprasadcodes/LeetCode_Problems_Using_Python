class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)<3:
            return 0
        if len(nums)==3:
            return sum(nums)
        nums.sort()
        print(nums)
        n=len(nums)
        res=float('inf')
        for i in range(n-2):
            l=i+1
            r=len(nums)-1
            if  i>0 and  nums[i]==nums[i-1]:
                continue
            min_sum=nums[i]+nums[l]+nums[l+1]
            if min_sum>=target:
                if abs(min_sum-target)<abs(res-target):
                    res=min_sum
                continue
            max_sum=nums[i]+nums[r]+nums[r-1]
            if max_sum<=target:
                if abs(max_sum-target)<abs(res-target):
                    res=max_sum
                continue
            while l<=r:
                s=nums[i]+nums[l]+nums[r]
                if abs(s-target)<abs(res-target):
                    res=s
                    print(res)
                if s >target:
                    r-=1
                else:
                    l+=1
        return res

s=Solution()
print(s.threeSumClosest([-1,2,1,-4],1))
print(s.threeSumClosest([0,0,0],1))