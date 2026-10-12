# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(root, localmin):
            if not root:
                return
            if root.val >= localmin:
                self.count+=1
            dfs(root.left, max(localmin, root.val))
            dfs(root.right, max(localmin, root.val))
        dfs(root, -101)
        return self.count
