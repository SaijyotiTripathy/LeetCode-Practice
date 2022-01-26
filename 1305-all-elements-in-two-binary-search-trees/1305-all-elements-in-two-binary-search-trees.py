# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        l=[]
        def dfs(root):
            if root:
                nonlocal l
                l.append(root.val)
                
                dfs(root.left)
                dfs(root.right)
        
        dfs(root1)
        dfs(root2)
        l.sort()
        return l