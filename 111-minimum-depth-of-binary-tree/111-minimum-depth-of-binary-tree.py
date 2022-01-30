# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        
        m,c=100000,0
        def dfs(root):
            if root:
                nonlocal c,m
                c+=1
                #print(c)
                if (root.left==None and root.right==None):
                    if c<m:
                        m=c
                
                dfs(root.left)
                dfs(root.right)
                c-=1
                return m
                
        
        return dfs(root)