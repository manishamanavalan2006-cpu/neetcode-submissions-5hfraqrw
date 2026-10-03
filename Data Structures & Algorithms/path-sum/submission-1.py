# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node,pathsum):
            if node is None:
                return False
            
            pathsum+=node.val

            if node.left is None and node.right is None:
                return pathsum==targetSum
            
            if dfs(node.left,pathsum):
                return True
            if dfs(node.right,pathsum):
                return True
            
            return False
        return dfs(root,0)
        