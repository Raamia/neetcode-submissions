class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = {}
        for i in range(numCourses):
            adjlist[i]  = []
        for u, v in prerequisites:
            adjlist[u].append(v)
        seen = set()
        def dfs(i):
            if i in seen:
                return False
            if i == []:
                return True
            seen.add(i)
            for nei in adjlist[i]:
                if not dfs(nei):
                    return False
            seen.remove(i)
            adjlist[i] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True