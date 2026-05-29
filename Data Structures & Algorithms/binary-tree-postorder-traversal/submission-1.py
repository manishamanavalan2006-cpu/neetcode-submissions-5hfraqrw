# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        if root is None:
            return []
        value1=self.postorderTraversal(root.left)
        result.extend(value1)
        value2=self.postorderTraversal(root.right)
        result.extend(value2)
        result.append(root.val)
        return result