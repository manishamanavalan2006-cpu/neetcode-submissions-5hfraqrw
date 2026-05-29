# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        if root is None:
            return []
        value1=self.inorderTraversal(root.left)
        result.extend(value1)
        result.append(root.val)
        value2=self.inorderTraversal(root.right)
        result.extend(value2)
        return result
