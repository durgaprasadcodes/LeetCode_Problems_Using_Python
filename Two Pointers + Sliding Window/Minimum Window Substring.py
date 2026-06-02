class Solution(object):
    def minWindow(self, s, t):
        
        if len(t)>len(s):
            return ""
        from collections import Counter,defaultdict

        need=Counter(t)

        l=0
        valid=0
        min_len=float('inf')
        res=""
        have=defaultdict(int)
        for r in range(len(s)):
            have[s[r]]+=1
            if s[r] in need and have[s[r]] == need[s[r]]:
                valid+=1
            
            while valid == len(need): 
                if min_len>(r-l+1):
                    res=s[l:r+1]
                    min_len=r-l+1
                have[s[l]]-=1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    valid-=1
                l+=1
        return res
                
s=Solution()
print(s.minWindow("ADOBECODEBANC","ABC"))

# Time Complexity: O(n)
# Space Complexity: O(m) 