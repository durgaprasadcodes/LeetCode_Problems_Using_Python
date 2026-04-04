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
        
        nums.sort()
        res=[]
        n=len(nums)
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
                if nums[i]+nums[j]+nums[n-2]+nums[n-1]<target:
                    continue
                left=j+1
                right=n-1
                while left <right:
                    print("Entered")
                    s=nums[i]+nums[j]+nums[left]+nums[right]
                    if s==target:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        left+=1
                        right-=1
                        while  left<right  and nums[left] == nums[left-1]:
                            left+=1
                        while  left<right and nums[right]==nums[right+1] :
                            right-=1
                    elif s>target:
                        right-=1
                    else:
                        left+=1
        return [list(i) for i in res]
s=Solution()
print(s.fourSum([1,0,-1,0,-2,2],0))     