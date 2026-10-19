class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz",
        }
        sol = []
        subset = ""
        def dfs(subset, sol, i):
            if i == len(digits):
                sol.append(subset)
                return
            for j in map[digits[i]]:
                subset+=j
                dfs(subset, sol, i+1)
                subset = subset[:-1]
        if not digits:
            return []
        dfs(subset, sol, 0)
        return sol