class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        if len(cardPoints)<k:
            return 0
        l=0
        r=len(cardPoints)-1
        cur_sum=max_sum=sum(cardPoints[:k])
        for l in range(k-1,-1,-1):
            cur_sum+=(cardPoints[r]-cardPoints[l])
            r-=1
            max_sum=max(max_sum,cur_sum)
        return max_sum

s=Solution()
print(s.maxScore([1,2,3,4,5,6,1],3))

# Time Complexity: O(k)
# Space Complexity: O(1)