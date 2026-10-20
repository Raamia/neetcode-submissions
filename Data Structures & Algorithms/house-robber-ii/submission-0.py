class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <=3:
            return max(nums)
        dp1 = [nums[0], max(nums[0],nums[1])]
        dp2 = [nums[1], max(nums[1],nums[2])]
        for i in range(2, len(nums)-1):
            temp = dp1[1]
            dp1[1] = max(dp1[1], nums[i]+dp1[0])
            dp1[0] = temp
        for i in range(3, len(nums)):
            temp = dp2[1]
            dp2[1] = max(dp2[1], nums[i]+dp2[0])
            dp2[0] = temp
        return max(dp1+dp2)