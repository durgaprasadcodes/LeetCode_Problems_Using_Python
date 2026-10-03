class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        ans = 0
        row_len = len(matrix)
        col_len = len(matrix[0])

        for top in range(row_len):
            nums = [0]*col_len
            for bottom in range(top,row_len):
                for col in range(col_len):
                    nums[col] += matrix[bottom][col]
                table = {0:1}
                cur_sum = 0
                cur_ans = 0
                for num in nums:
                    cur_sum += num
                    ans += table.get(cur_sum - target,0)
                    table[cur_sum] = table.get(cur_sum,0)+1
        return ans
