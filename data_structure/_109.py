# URL: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

# Main idea: 给定一个排完序的链表，通过这个排完序的链表去构建二叉平衡树

# 解题思路：
# （1）第一种：先将链表转化为数组，通过数组进行构建二叉平衡树（此时同108，就是多了一个构建过程）
# （2）第二种：（学习思路）和数组不同的是，链表不能直接分成两个部分，但是他总体的思想是和原本的是一致的，就是将此种数据结构（数组、链表）
# 进行切分为均等的两个部分，然后再进行递归，所以不管是数组还是链表，都是可以采用这种结构

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = self.__traverseLinkedList(head)
        return self.sortArrayToBST(nums)

    def sortArrayToBST(self, nums: list):
        if not nums:
            return None
        mid_index = len(nums) // 2
        root = TreeNode(nums[mid_index])
        root.left = self.sortArrayToBST(nums[:mid_index])
        root.right = self.sortArrayToBST(nums[mid_index + 1:])
        return root

    def __traverseLinkedList(self, head: ListNode):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res

    def sortedListToBST_learn(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        slow=fast=head
        prev=None
        while fast and fast.next:
            prev = slow
            slow=slow.next
            fast=fast.next.next
        if prev:
            prev.next = None
        else:
            head = None
        node = TreeNode(slow.val)
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(slow.next)

        return node

