class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        water = 0
        while left < right:
            if height[left] < height[right]:
                leftMax=max(leftMax,height[left])
                water += leftMax -height[left]
                left += 1
            else:
                rightMax = max(height[right],rightMax)
                water += rightMax - height[right]
                right -= 1
        return water