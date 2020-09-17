# URL:https://leetcode.com/problems/intersection-of-two-linked-lists/

# Main ideas:找给定的两个链表是否存在公共节点

# 解题思路：遍历两次可以得到答案，若两个链表存在公共节点，那么两者公共节点之后的长度一定是相等的，那么借助于这个思路，可以设置两个指针，
# 首先得到给定的两个链表的长度，然后让长链表的遍历指针先走长度差的步数，然后两个指针同时遍历，最后看两者是否相交即可

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curA, curB = headA, headB
        lenA, lenB = 0, 0
        # 分别计算两个链表的长度
        while curA is not None:
            lenA += 1
            curA = curA.next
        while curB is not None:
            lenB += 1
            curB = curB.next
        curA, curB = headA, headB
        if lenA > lenB:
            for i in range(lenA - lenB):
                curA = curA.next
        elif lenB > lenA:
            for i in range(lenB - lenA):
                curB = curB.next
        while curB != curA:
            curB = curB.next
            curA = curA.next
        return curA
