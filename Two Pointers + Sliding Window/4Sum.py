class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums)<4:
            return []
        if len(nums)==4 :
            return [nums] if sum(nums)==target else []
        res=[]
        n=len(nums)
        nums.sort()
        for i in range(n-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            if nums[i]+nums[i+1]+nums[i+2]+nums[i+3]>target:
                break
            if nums[i]+nums[n-1]+nums[n-2]+nums[n-3]<target:
                continue
            for j in range(i+1,n-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                if nums[i]+nums[j]+nums[j+1]+nums[j+2]>target:
                    break
                if nums[i]+nums[j]+nums[n-1]+nums[n-2]<target:
                    continue
                
                l=j+1
                r=len(nums)-1
                while l<r:
                    s=nums[i]+nums[j]+nums[l]+nums[r]
                    if s==target:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                        while l<r and nums[r]==nums[r+1]:
                            r-=1
                    elif s>target:
                        r-=1
                    else:
                        l+=1
        return res
        
s=Solution()
print(s.fourSum([1,0,-1,0,-2,2],0))
print(s.fourSum([2,2,2,2,2],8))
print(s.fourSum([0,0,0,0],0))

# Time Complexity: O(n^3)
# Space Complexity: O(1)