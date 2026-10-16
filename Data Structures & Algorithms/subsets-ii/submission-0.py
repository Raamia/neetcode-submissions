class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(sol, subset, i, nums):
            if i >= len(nums):
                sol.add(tuple(subset.copy()))
                return
            subset.append(nums[i])
            dfs(sol, subset, i+1, nums)
            subset.pop()
            dfs(sol, subset, i+1, nums)

        nums.sort() # O(nlogn)
        sol = set()
        subset = []
        dfs(sol, subset, 0, nums)
        return list(sol)