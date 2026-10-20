class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0:0}
        def dfs(i):
            if i in dp:
                return dp[i]
            if i == 0:
                return 0
            count = float("inf")
            for coin in coins:
                leftover = i-coin
                if leftover >= 0:
                    count = min(count, 1+dfs(leftover))
            dp[i] = count
            return count
        x = dfs(amount)
        if x > 100000:
            return -1
        return x