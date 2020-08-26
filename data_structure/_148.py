# URL:https://leetcode.com/problems/sort-list/

# Main idea:在时间复杂度为O(nlogn)，空间复杂度为O（1）的情况下排序链表

# 解题方式：
# （1）在题目中没有时间复杂度和空间复杂度的情况下，可以直接取下所有节点的值，然后排序，最后重构链表
# （2）在题目中给出了时间复杂度和空间复杂度的要求时，可以采用归并排序或者快排来实现
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """
        借助数组来实现
        :param head: 头节点
        :return: 排完序链表的头节点
        """
        vals = []
        p = head
        while p:
            vals.append(p.val)
            p = p.next
        vals.sort()
        h = None
        cur = None
        for val in vals:
            node = ListNode(val)
            if cur is None:
                cur = node
                h = node
            else:
                cur.next = node
                cur = cur.next
        return h

    def sortListMerge(self, head: ListNode) -> ListNode:
        """
        借助快速排序来完成题目的要求
        :param head: 原链表头节点
        :return: 排完序链表的头节点
        """
        if not head or not head.next:
            return head
        slow = fast = head
        pre = None
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        # 切断，分成两部分分别排序
        pre.next = None
        return self.merge(self.sortList(head), self.sortList(slow))

    def merge(self, left, right):
        res = cur = ListNode(0)
        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
                cur = cur.next
            else:
                cur.next = right
                right = right.next
                cur = cur.next
            if left:
                cur.next = left
            if right:
                cur.next = right
        return res.next
