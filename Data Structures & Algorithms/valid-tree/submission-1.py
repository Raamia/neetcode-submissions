class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjlist = {}
        for i in range(n):
            adjlist[i] = []
        for u, v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)
        seen = set()
        #cycle detection dfs
        def dfs(node, prev):
            if node in seen:
                return False
            seen.add(node)
            for i in adjlist[node]:
                if i == prev:
                    continue
                if not dfs(i, node):
                    return False
            return True
        return dfs(0, -1) and len(seen) == n