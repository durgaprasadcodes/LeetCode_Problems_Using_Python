class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        n = str(n)
        res = ''
        num_sum = 0
        for num in n:
            if num != '0':
                res+=num
                num_sum+=int(num)
        return int(res)*num_sum