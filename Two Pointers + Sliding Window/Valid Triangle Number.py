class Solution:
    def triangleNumber(self, nums)->int:
        if len(nums)<3:
            return 0
        ans=0
        nums.sort()
        for c in range(len(nums)-1,-1,-1):
            l=0
            r=c-1
            while l<r:
                if nums[0]+nums[1]>nums[c]:
                    ans+=((c+1)*(c)*(c-1))//6
                    break
                if nums[c-1]+nums[c-2]<=nums[c]:
                    continue
                if nums[l]+nums[r]>nums[c]:
                    ans+=r-l
                    r-=1
                else:
                    l+=1
        return ans
s=Solution()
print(s.triangleNumber( [2,2,3,3]))