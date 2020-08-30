# URL:https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Main idea: 给出先序和中序两个序列，重建二叉树

# 解题方式：
# （1）明确先序遍历序列和中序遍历序列的特点：先序中的每个节点在中序序列中都是将该节点划分为两个子树；
# （2）所以一直遍历先序，然后在中序中进行切分，最终即可得到相应的子树，递归进行下去。
# 先序遍历：根节点，左子树的先序遍历，右子树的先序遍历。
# 中序遍历：左子树的中序遍历，根节点，右子树的中序遍历。

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def buildTree(self, preorder, inorder:list) -> TreeNode:
        if not preorder or not inorder:
            return None
        root=TreeNode(preorder[0])
        index=inorder.index(preorder[0])
        root.left=self.buildTree(preorder[1:index+1],inorder[:index])
        root.right=self.buildTree(preorder[index+1:],inorder[index+1:])
        return root

