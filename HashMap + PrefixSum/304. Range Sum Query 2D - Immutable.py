# =============== BRUTE FORCE METHOD ===============
class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix
        self.prefix_sum = 0

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        totalSum = 0
        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                totalSum += self.matrix[row][col]
        return totalSum


# =========== OPTIMAL METHOD ==============


class NumMatrix:

    def __init__(self, matrix: list[list[int]]):

        rows = len(matrix)
        cols = len(matrix[0])

        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            for c in range(cols):
                self.prefix[r + 1][c + 1] = (
                    matrix[r][c]
                    + self.prefix[r][c + 1]
                    + self.prefix[r + 1][c]
                    - self.prefix[r][c]
                )

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return (
            self.prefix[r2 + 1][c2 + 1]
            - self.prefix[r1][c2 + 1]
            - self.prefix[r2 + 1][c1]
            + self.prefix[r1][c1]
        )
