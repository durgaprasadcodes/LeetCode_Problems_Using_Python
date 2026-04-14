class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n & n-1==0 if n else False
    
Solution().isPowerOfTwo(16)

# Time Complexity: O(1)
# Space Complexity: O(1)