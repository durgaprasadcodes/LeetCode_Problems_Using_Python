class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==1 or s ==" " :
            return 1
        r=set()
        cur_len=0
        i=0
        for j in range(len(s)):
            while s[j] in r:
                r.remove(s[i])
                i+=1
            r.add(s[j])
            cur_len=max(cur_len,j-i+1)
        return cur_len


        
        
s=Solution()
print(s.lengthOfLongestSubstring("ohvhjdml"))