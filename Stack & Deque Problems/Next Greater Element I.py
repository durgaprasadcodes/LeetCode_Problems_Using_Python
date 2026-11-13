class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:

        next_greater = {}
        stack = []
        for num in nums2[::-1]:
            while stack and num >= stack[-1]:
                stack.pop()
            next_greater[num] = -1 if not stack else stack[-1]
            stack.append(num)

        return [next_greater[num] for num in nums1]
