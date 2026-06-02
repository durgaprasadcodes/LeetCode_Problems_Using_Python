class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def check(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        l=0
        r=len(s)-1
        while l<=r:
            if s[l]!=s[r]:
                new1=s[l:r]
                new2=s[l+1:r+1]
                return check(l,r-1) or check(l+1,r)
            l+=1
            r-=1
        return True


s=Solution()
print(s.validPalindrome("abca"))

# Time Complexity  O(N)
# Space Complexity O(1)