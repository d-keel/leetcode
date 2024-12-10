class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #dfs
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
      
# T: O(n)  n = sum(nodes in tree)
# S: O(h)  h = height of the binary tree
