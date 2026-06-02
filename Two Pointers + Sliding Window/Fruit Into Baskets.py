class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        import collections
        d=collections.defaultdict(int)
        max_len=l=0
        for r in range(len(fruits)):
            d[fruits[r]]+=1
            while len(d)>2:
                d[fruits[l]]-=1
                if d[fruits[l]]==0:
                    del d[fruits[l]]
                l+=1
            max_len=max(max_len,r-l+1)
            print(max_len)
        return max_len

s=Solution()
print(s.totalFruit([1,2,1]))

# Time Complexity: O(n)
# Space Complexity: O(1) since the dictionary will hold at most 3 key-value pairs (the two types of fruits and their counts).