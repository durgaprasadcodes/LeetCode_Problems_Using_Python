class Solution(object):
    def numRescueBoats(self, p, limit):

        s=0
        c=0
        p.sort()
        l=0
        r=len(p)-1

        while l<=r:
            s=p[l]+p[r]
            if s<=limit:
                l+=1
                r-=1
            else:
                r-=1
            c+=1
        return c
        
s=Solution()
print(s.numRescueBoats([1,2], 3))

# Complexity :
# Time complexity: O(nlogn +n/2) => O(nlogn)
# Space complexity: O(1)