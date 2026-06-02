import collections
class Solution:
    def topKFrequent(self, nums, k) :
        
        buckets=[[] for _ in range(len(nums)+1)]
        d=collections.defaultdict(int)
        for i in nums:
            d[i]+=1
        for i,j in d.items():
            buckets[j].append(i)
        print(buckets)
        
        res=[]
        for r in range(len(buckets)-1,-1,-1):
            print(buckets[r])
            if buckets[r] and k!=0:
                res.extend(buckets[r])
                k-=len(buckets[r])
        return res
            
        
print(Solution().topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))