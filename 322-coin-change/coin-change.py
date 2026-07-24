class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def helper(rem):

            if rem == 0:
                return 0
            if rem < 0:
                
                return float('inf')
            minimum=float('inf')
            for coin in coins:
                result= 1+helper(rem-coin)
                minimum=min(minimum,result)
            return minimum
        return -1 if helper(amount)==float('inf') else helper(amount)
