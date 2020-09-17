# url:https://leetcode.com/problems/linked-list-cycle-ii/

# Main idea:给定一个链表，若链表存在环，那么找到环的入口，否则，返回None

# 解题思路：先找到相交点，然后一个指针从相交点出发，一个指针从头出发，即可找到最终的入口点

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        try:  ##如果有尾部，必然出错，进入except。
            Slow = head.next  ## 保证Slow和 Fast同时移动
            Fast = head.next.next
            while Slow != Fast:  ## Fast一直是Slow的两倍速度，这点很关键。
                Slow = Slow.next
                Fast = Fast.next.next
        except:
            return None
        Slow = head  ##让Slow从头开始，Fast保持上一步的位置
        while Slow != Fast:
            Slow = Slow.next
            Fast = Fast.next
        return Slow
