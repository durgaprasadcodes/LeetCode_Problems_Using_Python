class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s)<=1:
            return 1
        count = 0
        length=len(s)
        for i in range(length):
            left,right = i,i
            while left >= 0 and right < length and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            left,right = i,i+1
            while left >= 0 and right < length and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        return count
    
s=Solution()
print(s.countSubstrings("aba"))