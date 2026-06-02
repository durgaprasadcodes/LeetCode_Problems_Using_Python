class Solution(object):
    def merge(self, intervels):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervels)<=1:
            return intervels
        intervels.sort(key=lambda x:x[0])
        res=[intervels[0]]
        for curr in intervels[1:]:
            if curr[0] <=res[-1][-1]:
                res[-1][-1]=max(curr[1],res[-1][-1])
            else:
                res.append(curr)
        return res
        
s=Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))

# Time complexity: O(nlogn) because of sorting
# Space complexity: O(n) because of the result list