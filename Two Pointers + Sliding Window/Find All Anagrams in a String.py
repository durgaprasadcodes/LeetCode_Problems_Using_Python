class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res=[]
        j=0
        p_freq=[0]*26
        wind_freq=[0]*26
        for i in p:
            p_freq[ord(i)-97]+=1
        for i in s[:len(p)]:
            wind_freq[ord(i)-97]+=1
        if p_freq==wind_freq:
            res.append(j)
        for i in range(len(p),len(s)):
            wind_freq[ord(s[i-len(p)])-97]-=1
            wind_freq[ord(s[i])-97]+=1
            j+=1
            if p_freq==wind_freq:
                res.append(j)
        return res

    
s=Solution()
# print(s.findAnagrams("cbaebabacd","abc"))
print(s.findAnagrams("abab","ab"))

# TIME COMPLEXITY - O(N)
# SPACE COMPLEXITY -ON(N)
