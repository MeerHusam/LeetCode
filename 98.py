# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        output = []
        self = root

        def dfs(self):
            if self.left != None:
                dfs(self.left)
            output.append(self.val)
            if self.right != None:
                dfs(self.right)
            return

        if(self != None):
            dfs(self)
            
        # print(output)

        length = len(output) - 1
        for a in range(length):
            if output[a] >= output[a + 1]:
                return False
        return True
