class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjlist = {}
        seen = set()
        for i in range(n):
            adjlist[i] = []
        for u, v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)
        def dfs(node):
            if node in seen:
                return False
            seen.add(node)
            for i in adjlist[node]:
                dfs(i)
        count=0
        for i in range(n):
            if not i in seen:
                dfs(i)
                count+=1
        return count
