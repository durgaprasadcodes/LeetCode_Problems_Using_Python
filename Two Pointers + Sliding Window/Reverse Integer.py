class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign=1
        if x < 0:
            sign=-1
            x=-x
        x= int(str(x)[::-1])
        return 0 if x >pow(2,31) else x*sign

s=Solution()
print(s.reverse(-123))