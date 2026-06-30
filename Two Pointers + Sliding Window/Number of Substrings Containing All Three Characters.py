class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0
        freq = {'a':0,'b':0,'c':0}
        count = 0
        l=0
        n=len(s)
        for r in range(n):
            freq[s[r]]+=1
            while freq['a']>0 and freq['b']>0 and freq['c']>0:
                count+=n-r
                freq[s[l]]-=1
                l+=1
        return count