class Solution1:
    def maxFrequencyScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        result = left = curr = 0
        for right in range(len(nums)):
            curr += nums[right] - nums[(left + right) // 2]
            while not curr <= k:
                curr -= nums[((left + 1) + right) // 2] - nums[left]
                left += 1
            result = max(result, right - left + 1)
        return result


class Solution2:
    def maxFrequencyScore(self, nums, k):
        nums.sort()

        n = len(nums)

        prefix_sum = [0]

        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        l = 0
        ans = 0

        for r in range(n):

            m = (l + r) // 2
            median = nums[m]

            left_sum = prefix_sum[m] - prefix_sum[l]
            right_sum = prefix_sum[r + 1] - prefix_sum[m + 1]

            left_cost = median * (m - l) - left_sum
            right_cost = right_sum - median * (r - m)

            cost = left_cost + right_cost

            while cost > k:

                l += 1

                m = (l + r) // 2
                median = nums[m]

                left_sum = prefix_sum[m] - prefix_sum[l]
                right_sum = prefix_sum[r + 1] - prefix_sum[m + 1]

                left_cost = median * (m - l) - left_sum
                right_cost = right_sum - median * (r - m)

                cost = left_cost + right_cost

            ans = max(ans, r - l + 1)

        return ans
