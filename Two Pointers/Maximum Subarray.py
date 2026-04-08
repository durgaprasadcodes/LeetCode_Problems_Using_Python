class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = nums[0]
        curr = 0
        for num in nums:
            curr += num
            if curr > max_count:
                max_count = curr
            if curr < 0:
                curr = 0 

        return max_count