class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftmax, rightmax = height[0], height[-1]

        n = len(height)
        if n <= 2:
            return 0

        left, right = 1, n-2
        res = 0
        while left <= right:
            if leftmax > rightmax:
                if rightmax > height[right]:
                    res += rightmax - height[right]
                else:
                    rightmax = height[right]
                right -= 1
            else:
                if leftmax > height[left]:
                    res += leftmax - height[left]
                else:
                    leftmax = height[left]
                left +=1

        return res
s=Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
                
# Time complexity: O(n)
# Space complexity: O(1)