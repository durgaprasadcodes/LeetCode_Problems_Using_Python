class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        j=0
        for i in range(1,len(nums)):
            if nums[j]!=nums[i]:
                j+=1
                nums[j]=nums[i]
        return j+1

    
s=Solution()
print(s.removeDuplicates([1,1,2]))  # Output: 2
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))  # Output: 5

#  TIME COMPLEXITY: O(n)
#  SPACE COMPLEXITY: O(1)