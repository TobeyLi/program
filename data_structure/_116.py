# URL:https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

# Main idea:给定一颗完美二叉树，重新定义其结构，若当前节点的父节点存在右孩子，那么将当前节点定义一个指向右孩子的指针，否则
# 指向null。

# 解题方式：从根节点开始找到任意节点，将其左孩子指向右孩子。如果该节点已经指向了同层的其他节点，说明需要连接两个子树，
# 比如例子中的2->3,那么不仅要把2的左孩子4指向右孩子5，还要把2的右孩子5指向2的next节点的左孩子6。这样递归完成了，
# 每层就是单链表了。

import collections

# 定义的是一个完美二叉树的节点
class Node:
    def __init__(self,val,left=None,right=None,next=None):
        self.val=val
        self.left=left
        self.right=right
        self.next=next

class Solution:
    def connect(self, root:Node):
        if not root:
            return
        # 若当前节点存在右孩子
        if root.right:
            # 左孩子指针指向右孩子
            root.left.next = root.right
            # 若存在level order的右节点
            if root.next:
                root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root

    def connectQueue(self,root:Node):
        if not root:
            return
        queue=collections.deque()
        queue.append(root)
        while queue:
            lenQueue=len(queue)
            for i in range(lenQueue):
                node=queue.popleft()
                if i < lenQueue - 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
