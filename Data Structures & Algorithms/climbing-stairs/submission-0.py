class Solution:
    def climbStairs(self, n: int) -> int:
        # 1: 1
        # 2: 1, 2
        # 3: 1 1 1, 2 1, 1 2
        # 4: 1 1 1 1, 2 2, 2 1 1, 1 2 1, 1 1 2
        dp = [1, 2]
        if n < 3:
            return n
        for i in range(3,n+1):
            temp = dp[1]
            dp[1] = dp[1]+dp[0]
            dp[0] = temp
        return dp[1]