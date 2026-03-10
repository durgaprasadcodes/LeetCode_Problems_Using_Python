class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        res=0
        d={}
        i=0
        for j in range(len(fruits)):
            if  fruits[j] in d:
                d[fruits[j]]+=1
            else:
                d[fruits[j]]=1
            while len(d)>2:
                d[fruits[i]]-=1
                if not d[fruits[i]]:
                    d.pop(fruits[i])
                i+=1
            res=max(res,j-i+1)
        return res

s=Solution()
print(s.totalFruit([1,2,1]))

# Time Complexity: O(n)
# Space Complexity: O(1) since the dictionary will hold at most 3 key-value pairs (the two types of fruits and their counts).