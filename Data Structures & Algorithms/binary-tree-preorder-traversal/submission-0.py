# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        if root is None:
            return []
        result.append(root.val)
        value1=self.preorderTraversal(root.left)
        result.extend(value1)
        value2=self.preorderTraversal(root.right)
        result.extend(value2)
        return result