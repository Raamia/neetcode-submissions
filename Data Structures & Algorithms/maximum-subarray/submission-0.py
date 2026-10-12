class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        absmax = nums[0]
        localmax = 0
        for i in nums:
            localmax = max(localmax, 0)
            localmax +=i
            absmax = max(localmax, absmax)
        return absmax