# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, res):
            if not node:
                return 0
            if not node.left and not node.right:
                return res+ str(node.val)
            
            res+= str(node.val)
            return int(dfs(node.left,res))+int(dfs(node.right,res))
        
        return dfs(root,"")