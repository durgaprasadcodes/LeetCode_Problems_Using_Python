class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        p_a = [0]*26
        s_a = [0]*26
        res=[]
        l=0

        for ch in p:
            p_a[ord(ch)-97]+=1

        for ch in s[:len(p)]:
            s_a[ord(ch)-97]+=1
 
        if p_a == s_a:
            res.append(l)

        s_a[ord(s[l])-97]-=1
        l=1
        
        for i in range(len(p),len(s)):
            s_a[ord(s[i])-97]+=1
            if s_a == p_a:
                res.append(l)
            s_a[ord(s[l])-97]-=1
            l+=1
        return res

    
s=Solution()
# print(s.findAnagrams("cbaebabacd","abc"))
print(s.findAnagrams("abab","ab"))

# TIME COMPLEXITY - O(N)
# SPACE COMPLEXITY -ON(N)
