# URL :https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Main idea:求解二叉树的最大层数

# 解题方式：递归求解最大深度

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
