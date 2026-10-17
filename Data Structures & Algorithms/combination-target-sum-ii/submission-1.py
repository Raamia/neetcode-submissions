class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(sol, subset, i, target):
            if sum(subset) == target:
                sol.add(tuple(subset))
                return
            if sum(subset) > target or i == len(candidates):
                return
            subset.append(candidates[i])
            dfs(sol, subset, i+1, target)
            subset.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(sol, subset, i+1, target)
        candidates.sort()
        sol = set()
        subset = []
        dfs(sol, subset, 0, target)
        ret = []
        for i in sol:
            ret.append(list(i))
        return ret