# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        v= root.val
        flag=0
        def dfs(root):
            if root:
                if root.val!=v:
                    nonlocal flag
                    flag=1
                dfs(root.left)
                dfs(root.right)
        
        dfs(root)
        if flag==1:
            return False
        else:
            return True
        