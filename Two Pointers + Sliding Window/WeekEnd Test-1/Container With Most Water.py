class Solution :
    def maxArea(self,a):
        if len(a) == 1 :
            return 0
        i=0
        j=len(a)-1
        area=0
        while i<j:
            width = j-i
            height = min(a[i],a[j])
            area = max(area,width*height)
            
            if a[i]<a[j]:
                i+=1
            else:
                j-=1
        return area
    
s=Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
print(s.maxArea([1,1]))
        