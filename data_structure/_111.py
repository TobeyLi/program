# url: https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Main idea：求解二叉树最浅的深度

# 解题方式：本题和求解树的最大深度的题解的意思是一致的，那么只是需要比较树的最小深度即可
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            left_height = self.minDepth(root.left)
            right_height = self.minDepth(root.right)
            # when the node's left children and right children is None
            if root.left != None and root.right != None:
                return min(left_height, right_height) + 1
            else:
                return max(left_height, right_height) + 1
