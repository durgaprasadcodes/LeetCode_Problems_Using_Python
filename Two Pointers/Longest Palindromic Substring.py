class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        i=0
        j=len(s)-1
        res=""
        while i<=j:
            if s[i]==s[j]:
                cur_res=s[i:j+1] if j!=len(s)-1 else s[i:]
                def check(s):
                    return "" if s!=s[::-1] else s
                res=check(cur_res) if len(res)<len(check(cur_res)) else res
                i+=1
            j-=1
        return res

            
            
s=Solution()
print(s.longestPalindrome('cbbd'))