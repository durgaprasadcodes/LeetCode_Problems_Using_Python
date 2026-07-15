class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n
        # even = 0
        # odd  = 0
        # for i in range(1,2*n+1):
        #     if i & 1 == 0 :
        #         even+=i
        #     else:
        #         odd+=i
        # def gcd(a,b):
        #     if b==0:
        #         return a
        #     return gcd(b,a%b)
        # return gcd(odd,even)