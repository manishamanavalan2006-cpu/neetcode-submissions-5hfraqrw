class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def dfs(nums,left,right):
            if left>right:
                return None
            
            mid=left+(right-left)//2
            root=TreeNode(nums[mid])
            root.left=dfs(nums,left,mid-1)
            root.right=dfs(nums,mid+1,right)
            return root
        return dfs(nums,0,len(nums)-1)

            