# URL:https://leetcode.com/problems/binary-tree-level-order-traversal/

# Main idea:二叉树的层次遍历，每一层的结点分别采用一个数组记录

# 解题方式：采用层次遍历，然后每一层的结点采用一个新的list保存起来，加入到最终的list.
# 和普通层次遍历不同的是，我需要单独的记录每一层的结点的值

class TreeNode:
    def __init__(self,left,right,val):
        self.left=left
        self.right=right
        self.val=val

class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        stack,res=[],[]
        stack.append(root)
        while stack:
            temp,new=[],[]
            for node in stack:
                temp.append(node.val)
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)
            res.append(temp)
            stack=new
        return res
