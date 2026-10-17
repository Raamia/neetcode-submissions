class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subset = []
        sol = []
        def dfs(subset, sol, i, nums):
            if sum(subset) == target:
                sol.append(subset.copy())
                return
            if sum(subset) > target or i == len(nums):
                return
            subset.append(nums[i])
            dfs(subset, sol, i, nums)
            subset.pop()
            dfs(subset, sol, i+1, nums)
        dfs(subset, sol, 0, nums)
        return sol