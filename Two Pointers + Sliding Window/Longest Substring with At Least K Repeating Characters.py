class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        if k > len(s) or len(s) == 0:
            return 0

        res = 0

        # Try all possible counts of unique characters
        for target_unique in range(1, 27):

            d = [0] * 26
            l = 0

            unique = 0
            atleastk = 0

            for r in range(len(s)):

                right = ord(s[r]) - ord('a')

                if d[right] == 0:
                    unique += 1

                d[right] += 1

                if d[right] == k:
                    atleastk += 1

                while unique > target_unique:

                    left = ord(s[l]) - ord('a')

                    d[left] -= 1

                    if d[left] == k - 1:
                        atleastk -= 1

                    if d[left] == 0:
                        unique -= 1

                    l += 1

                if unique == target_unique and unique == atleastk:
                    res = max(res, r - l + 1)

        return res