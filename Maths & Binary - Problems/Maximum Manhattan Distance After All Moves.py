class Solution:
    def maxDistance(self, moves: str) -> int:
        if not moves:
            return ""
        x=y=0
        underscore = 0
        for ch in moves:
            if ch == 'R':
                x+=1
            elif ch == 'L':
                x-=1
            elif ch == 'U':
                y+=1
            elif ch == 'D':
                y-=1
                prev = 'y'
            else :
                underscore+=1
        return abs(x) + abs(y) + underscore
    