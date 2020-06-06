#url: https://leetcode.com/problems/partition-list/

# Main idea: 给出一个链表和一个数，要求重新对链表进行排序，小于这个数的，都排在这个数的左边，大于等于这个数的都排在这个数的右边。
# 要求排序的过程中要保持分开的两半中原本的数字的相对顺序不能变

# 最简单的做法是拿出所有的数字，然后再重新组成链表
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """
        借助与两个list进行操作，可以优化为只要一个list，这个list 的值都是存着大于x的内容，将这个list再次组成链表进行插入
        :param head:
        :param x:
        :return:
        """
        partition_1,partition_2=[],[]
        while head:
            if head.val>=x:
                partition_2.append(head.val)
            else:
                partition_1.append(head.val)
            head=head.next
        # 重新组成链表
        res=ListNode(0)
        current=res
        for i in partition_1:
            temp=ListNode(i)
            current.next=temp
            current=current.next
        for j in partition_2:
            temp=ListNode(j)
            current.next=temp
            current=current.next
        return res.next

    def partition_2(self,head:ListNode,x: int) -> ListNode:
        """
        不借助与额外的空间，先找到第一个大于等于x的值记为value，然后后面有小于x的值的话，直接将其插入到value前
        :param head:
        :param x:
        :return:
        """
        if not head or not head.next: return head
        dummy_head = prv = ListNode(float("inf"))
        prv.next = head
        while head and head.next:
            if head.val >= x and head.next.val<x:
                temp = head.next.next
                head.next.next = prv.next
                prv.next = head.next
                head.next = temp
            else:
                head = head.next
            if prv.next.val < x:
                prv=prv.next
        return dummy_head.next


