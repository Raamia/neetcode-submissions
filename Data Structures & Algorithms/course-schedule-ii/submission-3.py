class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        sol = []
        seen = set()
        adjlist = {}
        solset = set()
        for i in range(numCourses):
            adjlist[i] = []
        for u, v in prerequisites:
            adjlist[u].append(v)
        def dfs(node):
            if node in seen:
                return False
            if node in solset:
                return True
            seen.add(node)
            for i in adjlist[node]:
                if not dfs(i):
                    return False
            seen.remove(node)
            solset.add(node)
            sol.append(node)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return sol