class Solution:
    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:

        row_len = len(mat)
        col_len = len(mat[0])
        prefix_sum = [[0] * (col_len + 1) for _ in range(row_len + 1)]
        ans = [[0] * col_len for _ in range(row_len)]

        for r in range(row_len):
            for c in range(col_len):
                prefix_sum[r + 1][c + 1] = (
                    mat[r][c]
                    + prefix_sum[r][c + 1]
                    + prefix_sum[r + 1][c]
                    - prefix_sum[r][c]
                )
        for r in range(row_len):
            for c in range(col_len):
                top = max(0, r - k)  # don't go above 0
                btm = min(row_len - 1, r + k)  # don't go below last row

                left = max(0, c - k)  # don't go before 0
                right = min(col_len - 1, c + k)  # don't go beyond last column
                ans[r][c] = (
                    prefix_sum[btm + 1][right + 1]
                    - prefix_sum[top][right + 1]
                    - prefix_sum[btm + 1][left]
                    + prefix_sum[top][left]
                )
        return ans
