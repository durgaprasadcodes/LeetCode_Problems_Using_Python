class Solution:
    def goodDaysToRobBank(self, security: list[int], time: int) -> list[int]:

        ans = []
        n = len(security)
        for i in range(time, n - time):
            l = i - time
            r = i + time
            is_invalid = False

            while l < i:
                if security[l] < security[l + 1]:
                    is_invalid = True
                    break
                l += 1

            if is_invalid:
                continue

            while r > i:
                if security[r] < security[r - 1]:
                    break
                r -= 1

            if l == r:
                ans.append(i)

        return ans
