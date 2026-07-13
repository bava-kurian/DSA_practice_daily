from functools import lru_cache
class Solution:
    def numSquares(self, n: int) -> int:
        @lru_cache(None)
        def helper(rem):
            if rem==0:
                return 0
            
            ans=float('inf')

            i=1
            while i*i<=rem:

                ans= min(ans,1+helper(rem-i*i))
                i+=1
            return ans
        
        return helper(n)