class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if s=="":
            return 0

       #--------------- METHOD 1 QUIET FASTER --------

        l=max_len=0
        seen=set()
        for r in range(len(s)):

            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            max_len=max(max_len,r-l+1)

        return max_len
        # -------------- METHOD 2 ------------------

        # l=0
        # max_len=0
        # d=collections.defaultdict(int)

        # for r in range(len(s)):
        #     d[s[r]]+=1
        #     while d[s[r]]>1:
        #         d[s[l]]-=1
        #         l+=1
        #     max_len=max(max_len,r-l+1)
        # return max_len            
        
s=Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))

# Time Complexity: O(n) where n is the length of the string. Each character is visited at most twice (once by the right pointer and once by the left pointer).
# Space Complexity: O(min(m, n)) where m is the size of the character set and n is the length of the string. In the worst case, we may need to store all characters in the current window.