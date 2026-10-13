class Solution:
    def jump(self, nums: List[int]) -> int:
        furthest = 0
        count = 0
        inreach = 0
        for i in range(len(nums)-1):
            furthest = max(furthest, nums[i]+i)
            if i == inreach:
                inreach = furthest
                count+=1
        return count