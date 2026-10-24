"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        queue = deque()
        queue.append(node)
        copy = Node(node.val)
        map = {}
        map[node] = copy
        while queue:
            curr = queue.popleft()
            for i in curr.neighbors:
                if not i in map:
                    map[i] = Node(i.val)
                    queue.append(i)
                map[curr].neighbors.append(map[i])
        return map[node]