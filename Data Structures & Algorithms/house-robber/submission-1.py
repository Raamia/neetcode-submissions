class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        dp = [nums[0], max(nums[0],nums[1])]
        for i in range(2, len(nums)):
            temp = dp[1]
            dp[1] = max(dp[1], nums[i]+dp[0])
            dp[0] = temp
        return max(dp[1],dp[0])