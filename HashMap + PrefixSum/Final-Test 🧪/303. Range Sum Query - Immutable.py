class NumArray:

    def __init__(self, nums: list[int]):
        self.prefix_arr = []
        cur_sum = 0
        for num in nums:
            cur_sum += num
            self.prefix_arr.append(cur_sum)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_arr[right]
        return self.prefix_arr[right] - self.prefix_arr[left - 1]
