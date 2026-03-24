class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # def build(st):
        #     s=[]
        #     for i in st:
        #         if i!="#":
        #             s.append(i)
        #         elif s:
        #             s.pop()
        #     return "".join(s)
        # return build(s)==build(t)
       
        def build(s):
            i=len(s)-1
            ans=""
            while i>=0:
                if s[i]=='#':
                    i-=3
                else:
                    i-=1
                ans+=s[i] if s[i]!='#' else ""
            return ans
        print(build(s),build(t))
                
           
       
s=Solution()
print(s.backspaceCompare("ab##","c#d#"))