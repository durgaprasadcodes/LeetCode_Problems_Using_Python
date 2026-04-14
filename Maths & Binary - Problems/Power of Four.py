class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        while n%4==0:
            n//=4
        return n == 1
    
s=Solution()
print(s.isPowerOfFour(16))

# Time Complexity: O(log4(n))
# Space Complexity: O(1)