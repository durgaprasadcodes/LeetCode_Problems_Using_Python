class Solution:
    def longestKSubstr(self, s, k):
        # code here
        from collections import defaultdict
        d=defaultdict(int)
        l=0
        max_len=float('-inf')
        for r in range(len(s)):
            d[s[r]]+=1
            while len(d) > k:
                d[s[l]]-=1
                if d[s[l]]==0:
                    del d[s[l]]
                l+=1
            if len(d)==k:
                max_len=max(max_len,r-l+1)
        return max_len if max_len!=float('-inf') else -1
    
s=Solution()
print(s.longestKSubstr("aabacbebebe",3))