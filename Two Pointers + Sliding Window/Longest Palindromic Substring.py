class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s=="":
            return ""
        if len(s) == 1:
            return s

        longest=  ""

        def checkPalindrome(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
            
        for i in range(len(s)):
            oddlength = checkPalindrome(i,i)
            evenlength =checkPalindrome(i,i+1)

            if len(oddlength) > len(longest):
                longest = oddlength
            if len(evenlength)  > len(longest) :
                longest = evenlength
        return longest
    
s=Solution()
print(s.longestPalindrome("babad"))

# Time Complexity  O(N^2)
# Space Complexity O(1)