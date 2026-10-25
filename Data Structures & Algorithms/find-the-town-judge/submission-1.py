class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        candidates = [0]*(n+1)
        for u, v in trust:
            candidates[u] = -100000
            candidates[v]+= 1
        for i in range(1, len(candidates)):
            if candidates[i] == n-1:
                return i
        return -1