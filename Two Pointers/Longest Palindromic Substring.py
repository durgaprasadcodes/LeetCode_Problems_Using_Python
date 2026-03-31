class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        long=""
        def solve(i,j):
            while i>=0 and j<n and s[i]==s[j]:
                i-=1
                j+=1
            return s[i+1:j]
        for i in range(n):
            odd=solve(i,i)
            even=solve(i,i+1)
            
            if len(long)<len(odd):
                long=odd
            if len(long)<len(even):
                long=even
        return long
