class Solution:
    def minOperations(self, boxes: str) -> list[int]:

        n = len(boxes)
        if n == 1:
            return [0]

        ans = []
        total_ones = 0
        right_indices_sum = 0

        for idx, num in enumerate(boxes):
            if num == "1":
                total_ones += 1
                right_indices_sum += idx

        left_sum = 0
        left_indices_sum = 0
        right_sum = total_ones

        for idx, num in enumerate(boxes):
            if num == "1":

                left_sum += 1
                right_sum -= 1

                left_indices_sum += idx
                right_indices_sum -= idx

            cost = (
                idx * left_sum - left_indices_sum + right_indices_sum - idx * right_sum
            )
            ans.append(cost)
        return ans
