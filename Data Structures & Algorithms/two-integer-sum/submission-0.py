class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = i
        for i in range(len(nums)):
            if target-nums[i] in map and i != map[target-nums[i]]:
                return [i,map[target-nums[i]]]
