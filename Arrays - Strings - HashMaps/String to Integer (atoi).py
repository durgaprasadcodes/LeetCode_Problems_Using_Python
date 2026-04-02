class Solution:
    def myAtoi(self, s: str) -> int:

        i=0
        num=""
        n=len(s)
        while i<n and s[i]==" ":
            i+=1
        
        sign=1
        if i<n and (s[i] in '+-'):
            if s[i]=='-':
                sign =-1
            i+=1

        while i<n and s[i].isdigit():
            num+=s[i]
            i+=1
        
        if num=="":
            return 0

        num=int(num)
        if sign ==-1:
            num=-num

        INT_MAX=(2**31-1)
        INT_MIN=(-2**31)

        if num > INT_MAX:
            num=2**31-1
        elif num<INT_MIN:
            num=-2**31

        return num


