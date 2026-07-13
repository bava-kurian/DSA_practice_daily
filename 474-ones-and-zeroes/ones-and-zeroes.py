from functools import lru_cache
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @lru_cache(None)
        def helper(i,m1,n1):

            if i==len(strs):
                return 0
            ones=strs[i].count('1')
            zeros=strs[i].count('0')

            take=0    
            if ones<=n1 and  zeros<=m1:
                take=1+helper(i+1,m1-zeros,n1-ones)
            skip=helper(i+1,m1,n1)

            return max(take,skip)
        return helper(0,m,n)