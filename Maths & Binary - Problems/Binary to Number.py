class Solution:
    def B2N(self,number):
        if number == 0 or number == 1:
            return number
        number = str(number)
        sum = 0
        for i in number:
            sum = sum*2 + int(i)
        return sum
    
s=Solution()
print(s.B2N(1001)) 