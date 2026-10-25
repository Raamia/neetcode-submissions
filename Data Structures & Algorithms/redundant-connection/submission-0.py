class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        count = set()
        for u, v in edges:
            count.add(u)
            count.add(v)
        n = len(count)
        adjlist = {}
        for i in range(1,n+1):
            adjlist[i] = set()
        for u, v in edges:
            adjlist[u].add(v)
            adjlist[v].add(u)
        #try to pop, then dfs through
        def dfs(i):
            if i in seen:
                return False
            seen.add(i)
            for nei in adjlist[i]:
                dfs(nei)
            return True
        for i in range(len(edges)-1, -1, -1):
            adjlist[edges[i][1]].remove(edges[i][0])
            adjlist[edges[i][0]].remove(edges[i][1])
            seen = set()
            dfs(1)
            if len(seen) == n:
                return edges[i]
            adjlist[edges[i][1]].add(edges[i][0])
            adjlist[edges[i][0]].add(edges[i][1])