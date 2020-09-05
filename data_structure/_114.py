# URL:https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Main idea: 给出一颗二叉树，将其平展开来（所有节点做成一个链表的形状）

# 解题方式：
# （1）通过两个步骤，先遍历成一个链表，然后将其重建为一个树状链表,但是这样的话不满足条件，无法在原地进行转换；
# （2）查看提示：If you notice carefully in the flattened tree, each node's right child points to the next node of a
#              pre-order traversal.即每个节点的右子节点都指向先序遍历的下一个节点。
#  按照题目的理解，我们可以借助先序遍历的思想来解答
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack = [root]
        while stack:
            temp = stack[-1]
            stack.pop()
            # 存在左子树
            if temp.left:
                # 得到左子树
                r = temp.left
                # 找到当前节点左孩子的最右节点
                while r.right:
                    r = r.right
                # 按照hint进行替换
                r.right = temp.right
                temp.right = temp.left
                temp.left = None
            if temp.right:
                stack.append(temp.right)

    def flatten_1(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []
        self.preOrder(root, res)
        for i in range(len(res) - 1):
            res[i].left = None
            res[i].right = res[i + 1]

    def preOrder(self, root, res):
        if not root:
            return
        res.append(root)
        self.preOrder(root.left, res)
        self.preOrder(root.right, res)
