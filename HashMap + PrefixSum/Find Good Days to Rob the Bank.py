# ================= (N) ===============
class Solution:
    def goodDaysToRobBank(self, security: list[int], time: int) -> list[int]:
        n = len(security)
        if time * 2 >= n:
            return []
        if time == 0:
            return list(range(n))

        before = [0] * n
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                before[i] = before[i - 1] + 1

        after = [0] * n
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                after[i] = after[i + 1] + 1

        res = []
        for i in range(time, n - time):
            if before[i] >= time and after[i] >= time:
                res.append(i)

        return res


# ================ O(N*TIME) ================


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
