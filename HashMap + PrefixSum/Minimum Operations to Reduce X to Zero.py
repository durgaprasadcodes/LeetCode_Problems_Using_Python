
# Approch 1

class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        
        total = sum(nums)
        target = total - x

        if total == x:
            return len(nums)

        if target < 0:
            return -1

        cur_sum = 0
        ans = 0
        l = 0
        for r,num in enumerate(nums):
            cur_sum += num
            while cur_sum > target:
                cur_sum -= nums[l]
                l += 1
            if cur_sum == target:
                ans = max(ans,r-l+1)

        if 0 == ans:
            return -1
        return len(nums)-ans


        
# Approch 2
        
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        
        total = sum(nums)
        target = total - x

        if total == x:
            return len(nums)

        if target < 0:
            return -1

        cur_sum = 0
        ans = 0
        table = {0:-1}
        
        for idx,num in enumerate(nums):
            cur_sum += num
            if cur_sum-target in table:
                ans = max(ans,idx-table[cur_sum-target])
            if cur_sum not in table:
                table[cur_sum] = idx

        if ans == 0:
            return -1

        return len(nums) - ans
    
    
    
#       Approach	           Time Complexity	        Space Complexity	                       Why

#       Sliding Window         	O(n)	                    O(1)	             left and right each move at most n times
#       Prefix Sum + HashMap	O(n) average	            O(n)	             HashMap can store up to n prefix sums