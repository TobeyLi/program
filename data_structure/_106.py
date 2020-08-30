# URL:https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Main idea: 给出中序和后序两个序列，重建二叉树

# 解题方式：本题和105基本是一致的，只是一个是后序遍历，那么根节点就一定是最后一个节点，其他的建立方式基本一致

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: list, postorder: list) -> TreeNode:
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder[-1])
        index = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index + 1:], postorder[index:-1])
        return root