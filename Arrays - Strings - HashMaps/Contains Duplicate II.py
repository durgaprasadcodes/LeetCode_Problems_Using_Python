class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums)==len(set(nums)):
            return False
        d={}
        for idx in range(len(nums)):
            if nums[idx] in d and abs(d[nums[idx]]-idx)<=k:
                return True
            d[nums[idx]]=idx
        return False
    
s=Solution()
print(s.containsNearbyDuplicate([1,2,3,1],3))
print(s.containsNearbyDuplicate([1,0,1,1],1))
print(s.containsNearbyDuplicate([1,2,3,1,2,3],2))

# Time Complexity: O(n)
# Space Complexity: O(n)