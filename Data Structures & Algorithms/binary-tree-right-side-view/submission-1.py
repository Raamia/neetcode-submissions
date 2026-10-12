# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        if root:
            queue.append(root)
        sol = []
        while queue:
            last = -1
            lenq = len(queue)
            for i in range(lenq):
                node = queue.popleft()
                if node:
                    last = node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            sol.append(last)
        return sol
        