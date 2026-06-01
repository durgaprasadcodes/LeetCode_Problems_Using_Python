class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)>len(s2):
            return False
        
        s1_a = [0]*26
        s2_a = [0]*26

        for c in s1:
            s1_a[ord(c)-97]+=1
        
        l=0
        k=len(s1)

        for r in range(len(s2)):
            s2_a[ord(s2[r])-97]+=1
            while r-l+1>k:
                s2_a[ord(s2[l])-97]-=1
                l+=1
            if s1_a==s2_a:
                return True
                
        return False
    
s=Solution()
print(s.checkInclusion("ab",  "eidbaooo"))