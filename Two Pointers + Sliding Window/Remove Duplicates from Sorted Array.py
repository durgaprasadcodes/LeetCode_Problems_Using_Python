class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return 1
        prev=0
        for cur in range(1,len(nums)):
            if nums[prev] != nums[cur]:
                prev+=1
                nums[prev] = nums[cur]
        return prev +1

    
s=Solution()
print(s.removeDuplicates([1,1,2]))  # Output: 2
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))  # Output: 5

#  TIME COMPLEXITY: O(n)
#  SPACE COMPLEXITY: O(1)