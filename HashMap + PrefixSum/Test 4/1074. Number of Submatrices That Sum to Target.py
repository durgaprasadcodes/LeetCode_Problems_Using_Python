class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:

        row_len = len(matrix)
        col_len = len(matrix[0])
        ans = 0
        for top in range(row_len):
            col_sum = [0] * col_len
            for btm in range(top, row_len):
                for col in range(col_len):
                    col_sum[col] += matrix[btm][col]
                table = {0: 1}
                cur_sum = 0
                for num in col_sum:
                    cur_sum += num
                    ans += table.get(-target + cur_sum, 0)
                    table[cur_sum] = table.get(cur_sum, 0) + 1
        return ans
