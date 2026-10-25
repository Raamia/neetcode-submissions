class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjlist = {}
        def dfs(node, prev):
            if node in seen:
                return True
            seen.add(node)
            for i in adjlist[node]:
                if i == prev:
                    continue
                if dfs(i, node):
                    return True
            return False

        for i in range(len(edges)):
            seen = set()
            if edges[i][1] not in adjlist:
                adjlist[edges[i][1]] = []
            adjlist[edges[i][1]].append(edges[i][0])
            if edges[i][0] not in adjlist:
                adjlist[edges[i][0]] = []
            adjlist[edges[i][0]].append(edges[i][1])
            if dfs(edges[i][1], -1):
                return edges[i]
        