class Solution(object):
    def findMedianSortedArrays(self, a, b):
            c=[]
            i=j=k=0
            while (i<len(a) and j <len(b)):
                if a[i]<b[j]:
                    c.append(a[i])
                    i+=1
                else:
                    c.append(b[j])
                    j+=1

            while i<len(a):
                c.append(a[i])
                i+=1
            while j<len(b):
                c.append(b[j])
                j+=1

            num=len(c)//2

            if len(c)%2==0:
                return (c[num-1]+c[num])/2
            return c[num]

a=[1,2]
b=[3,4]
print(Solution().findMedianSortedArrays(a,b))