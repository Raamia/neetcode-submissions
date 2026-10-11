# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if p and not q:
                return False
            if q and not p:
                return False
            if not q and not p:
                return True
            if p.val != q.val:
                return False
            left = isSameTree(p.left, q.left)
            right = isSameTree(p.right, q.right)
            return left and right
        if not subRoot:
            return True
        if not root:
            return False
        if isSameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
            