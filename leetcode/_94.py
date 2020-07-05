# URL：https://leetcode.com/problems/binary-tree-inorder-traversal/

# Main idea:中序遍历二叉树，要求采用非递归的方式来做

# 解题方式：
# 题目是比较简单的，主要是采用非递归的方式来做，主要是需要借助于一个额外的栈即可，同样，本人也会给出递归和非递归的
# 两种解题方法

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.inOrderRes=[]
    @staticmethod
    def inorderTraversal(self, root: TreeNode):
        """
        采用递归的方式来中序遍历二叉树,此时必须要借助一个额外的变量才可以,accept是无压力的
        :param root:
        :return: 中序遍历的序列
        """

        if not root:
            return
        self.inorderTraversal(root.left)
        self.inOrderRes.append(root.val)
        self.inorderTraversal(root.right)

        return self.inOrderRes
    @staticmethod
    def inorderTraversal_iterative(self, root: TreeNode):
        """
        采用迭代的方式进行中序遍历，需要借助栈
        :param root:
        :return:
        """
        stack,res=[],[]
        cur=root
        while cur or len(stack)>0:
            while cur:
                stack.append(cur)
                cur=cur.left
            cur=stack.pop()
            res.append(cur.val)
            cur=cur.right
        return  res
