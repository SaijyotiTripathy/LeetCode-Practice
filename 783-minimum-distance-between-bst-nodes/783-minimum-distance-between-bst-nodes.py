# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        l=[]
        def dfs(root):
            if root:
                nonlocal l
                l.append(root.val)
            
                dfs(root.left)
                dfs(root.right)
        
        dfs(root)
        l.sort()
        #print(l)
        m= l[-1]-l[0]
        for i in range(len(l)-1):
            if m> l[i+1]-l[i]:
                m= l[i+1]-l[i]
        return m
        