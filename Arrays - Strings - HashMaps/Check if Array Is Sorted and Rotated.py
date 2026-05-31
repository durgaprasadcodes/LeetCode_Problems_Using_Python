class Solution:
    def check(self, nums) -> bool:
        n=len(nums)
        count=1
        
        for  i in range(1,n*2):
            if nums[(i-1)%n] <= nums[i%n]:
                count+=1
            else:
                count=1
            if count == n:
                return True
        return  n==1
    
s=Solution()
print(s.check([3,4,5,1,2]))
