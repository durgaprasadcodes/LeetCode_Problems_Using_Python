class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==1 or s ==" " :
            return 1
        res=""
        cur_len=0
        i=0
        for j in range(1,len(s)):
            if s[j]==s[i]:
                cur_len=max(cur_len,j-i+1)
                i+=1
                print(s[i],s[j])
        return cur_len
        
        
s=Solution()
print(s.lengthOfLongestSubstring("anviaj"))