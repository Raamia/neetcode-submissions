class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(sol, subset, i, nums):
            if i >= len(nums):
                sol.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(sol, subset, i+1, nums)
            subset.pop()

            dfs(sol, subset, i+1, nums)
        sol = []
        subset = []
        dfs(sol, subset, 0, nums)
        return sol