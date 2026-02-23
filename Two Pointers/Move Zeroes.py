class Solution(object):
    def moveZeroes(self, a):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(a)<=1:
            return a
        i = 0
        for j in range(len(a)):
            if a[j] != 0:
                a[i], a[j] = a[j], a[i]
                i += 1    
        return a
s=Solution()
print(s.moveZeroes([0,0,0,0,1,0,3,12,0,0,11,0,2,2,0,3,4]))