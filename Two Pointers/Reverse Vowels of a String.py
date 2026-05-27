class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s=="":
            return ""
        l=0
        r=len(s)-1
        a=list(s)
        st="aeiou"
        while l<r:
            while l<r and a[l].lower() not in st:
                l+=1
            while l<r and a[r].lower() not in st:
                r-=1
            a[l],a[r] = a[r],a[l]
            l+=1
            r-=1
        return "".join(a) 
    
s=Solution()
print(s.reverseVowels("hello"))