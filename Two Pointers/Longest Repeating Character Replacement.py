class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        l= 0
        majority = 0
        d=defaultdict(int)
        res= 0
        for r in range(len(s)):
            d[s[r]]+=1
            majority = majority if majority >d[s[r]] else d[s[r]]

            if (r-l+1) - majority > k:
                d[s[l]]-=1
                l+=1
            res = res if res > r-l+1 else r-l+1
        return res
s=Solution()
print(s.characterReplacement("ABAB",2))
print(s.characterReplacement("ABAABBABA",2))
print(s.characterReplacement("AABABBA",1))
                        
            