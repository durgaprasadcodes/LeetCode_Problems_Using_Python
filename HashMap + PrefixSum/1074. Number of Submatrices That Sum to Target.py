class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        
    
        rows = len(matrix)
        cols = len(matrix[0])
        answer = 0

        for top in range(rows):

            col_sum = [0] * cols

            for bottom in range(top, rows):

                for c in range(cols):
                    col_sum[c] += matrix[bottom][c]

                prefix = 0
                count = {0: 1}

                for num in col_sum:
                    prefix += num

                    if prefix - target in count:
                        answer += count[prefix - target]

                    count[prefix] = count.get(prefix, 0) + 1

        return answer