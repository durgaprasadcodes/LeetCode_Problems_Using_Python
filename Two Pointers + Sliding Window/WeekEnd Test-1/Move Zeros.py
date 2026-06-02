class Solution(object):
    def moveZeroes(self, a):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(a) <=1:
            return a
        i=0
        for j in range(len(a)):
            if a[j]!=0:
                a[j],a[i]=a[i],a[j]
                i+=1
        return a
    
s=Solution()
print(s.moveZeroes([0,1,0,3,12]))