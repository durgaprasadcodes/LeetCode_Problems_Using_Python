class Solution:
    def convert(self, s: str, numRows: int) -> str:
            if len(s)==1:
                return s
            i=0
            d=1
            res=""
            row=[[] for _ in range(numRows)]
            for c in s:
                row[i].append(c)
                if i<=0:
                    d=1
                    i=0
                if i==numRows-1:
                    d=-1
                i+=d
            for i in row:
                res+="".join(i)
            return res