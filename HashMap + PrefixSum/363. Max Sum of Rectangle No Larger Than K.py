class Solution:
    def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        
        row_len = len(matrix)
        col_len = len(matrix[0])
        ans = 0

        for top in range(row_len):
            col_sum = [0]*col_len
            for btm in range(top,row_len):
                for col in range(col_len):
                    col_sum[col] += matrix[btm][col]
                
                prefix = 0
