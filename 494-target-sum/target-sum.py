from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def helper(i,sum):
            if i==len(nums):
                return 1 if sum==target else 0
            
            plus=helper(i+1,sum+nums[i])

            minus=helper(i+1,sum-nums[i])

            return plus+minus
        return helper(0,0)