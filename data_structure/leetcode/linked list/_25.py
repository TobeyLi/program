# URL:https://leetcode.com/problems/reverse-nodes-in-k-group/

# Main idea:给出一个链表和一个整数k，对链表中的每k个一组进行反转。
# 如给出链表: 1->2->3->4->5
# 当k=2时，返回的内容是: 2->1->4->3->5
# 当k=3时，返回的内容时: 3->2->1->4->5

# 注意：
#  （1）只能使用常数的空间
#  （2）不能改变节点内的值（节点是一个整体）

# 解题方式：对于本题，其处理方式还是和92基本一直，但是一个不同点是

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        dummyNode = ListNode(-1)
        dummyNode.next = head
        pre = dummyNode
        stack, satisfyK = [], True
        cur = head
        while cur:
            for _ in range(k):
                if cur:
                    stack.append(cur)
                    cur = cur.next
                else:
                    satisfyK = False
                    break
            if not satisfyK:
                break
            nextHead = cur

            # reverse
            while stack:
                node = stack.pop()
                pre.next = node
                pre = node
            pre.next = nextHead
        return dummyNode.next
