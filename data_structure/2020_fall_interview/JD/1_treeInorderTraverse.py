# 二叉树中序遍历
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.left=left
        self.right=right
        self.val=val

def inorderTraverse(root:TreeNode):
    if not root:
        return
    inorderTraverse(root.left)
    print(root.val)
    inorderTraverse(root.right)