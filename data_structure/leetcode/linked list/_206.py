# URL:https://leetcode.com/problems/reverse-linked-list/

# Main idea:反转链表

# 解题方式：
# （1）借助与两个指针，每次记录当前节点，当前节点的前置节点和后置节点，然后进行换向操作。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        pre = None
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre
