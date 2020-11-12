# URL:https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

# Main idea: 给定一颗二叉树，而不是和116一样的完美二叉树，那么需要将其每一层定义为一个单链表

# 解题方式：操作方式是和116一致，只是这颗二叉树不是完美二叉树,本题可以借助与一个常数的空间队列，通过队列去进行判断每次一层的情况，
# 116题也可以进行这样的操作

import collections

# 定义的是一个完美二叉树的节点
class Node:
    def __init__(self,val,left=None,right=None,next=None):
        self.val=val
        self.left=left
        self.right=right
        self.next=next

class Solution:
    def connect(self, root: Node):
        if not root:
            return
        queue = collections.deque()
        queue.append(root)
        while queue:
            _len = len(queue)
            for i in range(_len):
                node = queue.popleft()
                if i < _len - 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root