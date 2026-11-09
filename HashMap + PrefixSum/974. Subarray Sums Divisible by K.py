class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        cur_sum = 0
        table = {0: 1}
        ans = 0

        for num in nums:
            cur_sum += num
            reminder = cur_sum % k
            ans += table.get(reminder, 0)
            table[reminder] = table.get(reminder, 0) + 1

        return ans
