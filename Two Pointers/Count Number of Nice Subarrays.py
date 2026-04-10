class Solution(object):
    def numberOfSubarrays(self, nums, k):

        def subArray(nums,k):
            if k<0:
                return 0
            l=0
            c=0
            run_sum=0
            for r in range(len(nums)):
                run_sum+=nums[r]%2
                while run_sum>k:
                    run_sum-=nums[l]%2
                    l+=1
                c+=(r-l+1)
            return c
        a=subArray(nums,k)
        b=subArray(nums,k-1)

        return a-b