class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if not fruits:
            return 0
        import collections
        l = 0
        max_len=0
        d=collections.defaultdict(int)
        for r in range(len(fruits)):
            d[fruits[r]]+=1

            while l<r and  len(d)>2:
                d[fruits[l]]-=1
                if d[fruits[l]] == 0:
                    del d[fruits[l]]
                l+=1

            max_len=max(max_len,r-l+1)
        return max_len
    
s=Solution()
print(s.totalFruit([1,2,1]))

# Time Complexity: O(n)
# Space Complexity: O(1) 