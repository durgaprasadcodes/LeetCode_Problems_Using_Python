class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="":
            return 0
        if len(s)==1:
            return 1
        l=0
        st=set()
        max_len=0
        for i in range(len(s)):
            while s[i] in st:
                st.remove(s[l])
                l+=1
            st.add(s[i])
            max_len=max(max_len,i-l+1)
        return max_len
s=Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
# Time Complexity: O(n)
# Space Complexity: O(n)