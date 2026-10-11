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
