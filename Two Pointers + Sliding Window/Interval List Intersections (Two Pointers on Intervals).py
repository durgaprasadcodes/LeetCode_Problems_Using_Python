class Solution(object):
    def intervalIntersection(self, l1,l2):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        if not l1 or not l2:
            return []
        i=0
        j=0
        res=[]
        while i<len(l1) and j<len(l2):
            start=max(l1[i][0],l2[j][0])
            end=min(l1[i][-1],l2[j][-1])
            l1_end=l1[i][-1]
            l2_end=l2[j][-1]
            if start<=end:
                res.append([start,end])
            if l1_end<l2_end:
                i+=1
            else:
                j+=1

        return res