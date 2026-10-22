class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total = sum(nums)
        left = 0
        ans = []

        for i, x in enumerate(nums):
            right = total - left - x

            ans.append(
                x * i - left +
                right - x * (n - i - 1)
            )

            left += x

        return ans