# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l=[]
        def dfs(root):
            if root:
                if (root.left==None and root.right==None):
                    nonlocal l
                    l.append(root.val)
                dfs(root.left)
                dfs(root.right)
                return l
        
        dfs(root1)
        l= dfs(root2)
        #print(l)
        h= len(l)//2
        if l[:h]==l[h:]:
            #print(l[:h],l[h:])
            return True
        else:
            return False
        
        