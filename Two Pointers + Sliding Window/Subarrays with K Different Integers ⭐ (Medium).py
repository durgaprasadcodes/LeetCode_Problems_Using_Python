class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        n = len(nums)
        count = [0] * (n + 1)
        res = l = c = 0

        for r in range(n):
            count[nums[r]] += 1
            if count[nums[r]] == 1:
                k -= 1

            if k < 0:
                count[nums[l]] -= 1
                l += 1
                k += 1
                c = 0

            if k == 0:
                while count[nums[l]] > 1:
                    count[nums[l]] -= 1
                    l += 1
                    c += 1

                res += (c + 1)

        return res
        
s=Solution()
print(s.subarraysWithKDistinct([1,2,1,2,3], 2)) # 7

# Time Complexity: O(n)
# Space Complexity: O(n)