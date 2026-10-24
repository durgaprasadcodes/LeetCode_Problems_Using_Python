# =============== BRUTE FORCE ==================
class Solution:

    def minOperations(self, boxes: str) -> list[int]:
        n = len(boxes)
        if n == 1:
            return [0]

        ans = []
        for i in range(len(boxes)):
            cur_ans = 0
            for j in range(len(boxes)):
                if i != j and boxes[j] == "1":
                    cur_ans += abs(j - i)
            ans.append(cur_ans)

        return ans
