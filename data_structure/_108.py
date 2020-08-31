# URL:https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Main idea:给定一个升序序列，将其建造成一个二叉平衡树

# 解题方式：

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list) -> TreeNode:
        if not nums:
            return None
        mid_index=len(nums)//2
        root=TreeNode(nums[mid_index])
        root.left=self.sortedArrayToBST(nums[:mid_index])
        root.right=self.sortedArrayToBST(nums[mid_index+1:])
        return root
