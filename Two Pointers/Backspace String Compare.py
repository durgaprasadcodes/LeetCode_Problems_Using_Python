class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        import collections
        s1=collections.defaultdict(int)
        t1=collections.defaultdict(int)
        p=1
        
        for i in range(len(s)):
            if s[i]=="#":
                while  i<len(s) and s[i]=="#":
                    s1[s[i-p]]-=1
                    if s1[s[i-p]]==0:
                        del s1[s[i-p]]
                    i+=1
                    p+=1
            else:
                s1[s[i]]+=1
        print(s1)
            
        p=1
        
        for i in range(len(t)):
            if t[i]=="#":
                while  i<len(t) and t[i]=="#":
                    t1[t[i-p]]-=1
                    if t1[t[i-p]]<=0:
                        del t1[t[i-p]]
                    i+=1
                    p+=1
            else:
                t1[t[i]]+=1
        print(t1)
        return s1==t1
s=Solution()
print(s.backspaceCompare("ab##","c#d#"))