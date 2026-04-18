import collections
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        if len(s)==1:
            return 1
        counter = collections.defaultdict(int)
        majority = 0
        res = 0
        left = 0
        for right in range(len(s)):

            counter[s[right]] += 1
            
            if counter[s[right]] > counter[majority]:
                majority = s[right]
            
            if right - left + 1 - counter[majority] > k:
                counter[s[left]] -= 1
                left += 1
            
            res = right - left + 1

        return res
s=Solution()
print(s.characterReplacement("ABAB",2))
print(s.characterReplacement("ABAABBABA",2))
print(s.characterReplacement("AABABBA",1))
                        
            