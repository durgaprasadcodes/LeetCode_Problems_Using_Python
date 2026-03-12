class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        n = len(fruits)
        used = [False] * n
        unplaced = 0

        for fruit in fruits:
            placed = False
            for i, cap in enumerate(baskets):
                if not used[i] and cap >= fruit:
                    used[i] = True
                    placed = True
                    break
            if not placed:
                unplaced += 1

        return unplaced
    
if __name__ == "__main__":
    s = Solution()
    # Expected: 1
    print(s.numOfUnplacedFruits([4, 2, 5], [3, 5, 4]))
    # Expected: 0
    print(s.numOfUnplacedFruits([3, 6, 1], [6, 4, 7]))
