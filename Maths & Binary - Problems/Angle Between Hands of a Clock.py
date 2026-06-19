class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour = 0 if hour == 12 else hour
        ans =  abs(30*hour - 5.5*minutes)
        return  min(ans ,360-ans)