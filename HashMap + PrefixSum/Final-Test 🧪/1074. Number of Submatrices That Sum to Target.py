class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:

        rows = len(matrix)
        cols = len(matrix[0])
        ans = 0
        for top in range(rows):
            col_sum = [0] * cols
            for btm in range(top, rows):
                for col in range(cols):
                    col_sum[col] += matrix[btm][col]
                cur_sum = 0
                table = {0: 1}
                print(col_sum)
                for num in col_sum:
                    cur_sum += num
                    ans += table.get(cur_sum - target, 0)
                    table[cur_sum] = table.get(cur_sum, 0) + 1
        return ans
