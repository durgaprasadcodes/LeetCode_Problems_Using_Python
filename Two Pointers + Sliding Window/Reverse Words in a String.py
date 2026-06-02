class Solution:
    def reverseWords(self, s: str) -> str:
        if s=="":
            return ""
        
        stk=[]
        res=""

        for r in s:
            if r==" ":
                if res!="":
                    stk.append(res)
                res=""
            res+=r if r!=" " else ""
        
        stk.append(res)
        return " ".join(stk[::-1]).strip()

s=Solution()
print(s.reverseWords("Hello World"))
print(s.reverseWords("  Hello   World  "))

# Time Complexity: O(n)
# Space Complexity: O(n)