class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k<=1:
            return 0
        count=0
        pdt=1
        l=0
        for i in range(len(nums)):
            pdt*=nums[i]
            while pdt>=k and l<=i:
                pdt//=nums[l]
                l+=1
            count+=(i-l+1)
        return count
s=Solution()
print(s.numSubarrayProductLessThanK([10,5,2,6],100))
# Time Complexity: O(n)
# Space Complexity: O(1)