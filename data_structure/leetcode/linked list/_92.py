# url:https://leetcode.com/problems/reverse-linked-list-ii/

# Main idea:给出两个数m,n，反转一个链表，区间要求为：[m,n]
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL

# 解题思路：
# 方法1：题目已经说明，m，n是符合条件的，所以不用去进行判断有效性，那么我们需要做的，最简单的方法是借助于额外的数组来进行处理
# 方法2：链表相关的题常见的解法；对于链表的问题，根据以往的经验一般都是要建一个dummy node，连上原链表的头结点，这样的话就算头结点变动了，
# 我们还可以通过dummy->next来获得新链表的头结点。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        """
        借助额外的数组去进行数组重建，时间复杂度O(n),空间复杂度O(n)
        :param head:
        :param m:
        :param n:
        :return:
        """
        values=[]
        while head:
            values.append(head.val)
            head=head.next
        # reverse
        temp=values[m-1:n]
        temp.reverse()
        for i in range(m-1,n):
            values[i]=temp[i-m+1]
        # reconstruct
        res=tail=ListNode(0)
        for i in range(len(values)):
            node=ListNode(values[i])
            tail.next=node
            tail=node
        return res.next

    def reverseBetweenPointer(self, head: ListNode, m: int, n: int) -> ListNode:
        """
        不借助额外的数组，只是需要再新建一个节点和头插法进行结合起来，时间复杂度O(n),空间复杂度O(1)
        :param head:
        :param m:
        :param n:
        :return:
        """
        dummyNode=ListNode(0)
        dummyNode.next=head
        pre=dummyNode
        # find the mth node
        for _ in range(m-1):
            pre=pre.next
        # record the first node to reverse
        cur=pre.next
        for _ in range(m,n):
            node=cur.next
            cur.next=node.next
            node.next=pre.next
            pre.next=node
        return dummyNode.next


if __name__ == '__main__':
    solution=Solution()
    # construct list
    head=ListNode(0)
    tail=head
    for i in range(1,6):
        node=ListNode(i)
        tail.next=node
        tail=node
    solution.reverseBetween(head.next,2,4)