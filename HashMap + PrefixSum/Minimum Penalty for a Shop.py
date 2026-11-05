class Solution:
    def bestClosingTime(self, customers: str) -> int:
        min_penalty = 0
        hour = 0
        curr_penalty = 0

        for i, ch in enumerate(customers, start=1):
            if ch == "Y":
                curr_penalty -= 1
            else:
                curr_penalty += 1

            if curr_penalty < min_penalty:
                min_penalty = curr_penalty
                hour = i

        return hour
