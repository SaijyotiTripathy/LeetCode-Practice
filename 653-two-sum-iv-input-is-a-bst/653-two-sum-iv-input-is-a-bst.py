# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        l=[]
        flag=0
        def dfs(root):
            if root:
                if (k-root.val) in l:
                    nonlocal flag
                    flag=1
                    return
                else:
                    l.append(root.val)
                dfs(root.left)
                dfs(root.right)
        
        dfs(root)
        if flag==1:
            return True
        else:
            return False
        