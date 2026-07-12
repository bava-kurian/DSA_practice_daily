from functools import lru_cache

class Solution:
    def minSteps(self, n: int) -> int:
        @lru_cache(None)
        def helper(screen, clipboard):
            if screen == n:
                return 0

            if screen > n:
                return float('inf')

            copy = float('inf')
            if screen != clipboard:
                copy = 1 + helper(screen, screen)

            paste = float('inf')
            if clipboard > 0:
                paste = 1 + helper(screen + clipboard, clipboard)

            return min(copy, paste)

        return helper(1, 0)