class Solution(object):
    def characterReplacement(self, s, k):
        if len(s)==1:
            return 1
        max_len=0
        for target in set(s):
            i=0
            count=0
            for j in range(len(s)):
                if s[j]!=target:
                    count+=1
                    while count>k:
                        if s[i]!=target:
                            count-=1
                        i+=1
                max_len=max(max_len,j-i+1)
        return max_len
s=Solution()
print(s.characterReplacement("ABAB",2))
print(s.characterReplacement("ABAABBABA",2))
print(s.characterReplacement("AABABBA",1))
                        
            