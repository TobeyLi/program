# url:https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

#Main idea:删除链表中出现重复的数字，保留在list中只出现一次的数字,返回去重之后的list
# 做法：设计两个指针，一个指向最后一个不是重复的元素，一个是工作指针，两个指针为i，j,其中i为工作指针
# 遍历方式：在j之前都不存在重复的元素；
# 1.当i.val不等于j.val时，i,j指针同时移动；
# 2.当i.val==j.val时，i++;直到i.val不等于j.val,然后j.next=i

# 本题思想的方式较为普通，最巧妙的方式是设计了一个头节点，然后保证后面所哟节点的处理方式都是一样的

class ListNode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

class Solution:
    def deleteDuplicates(self, head):
        res=ListNode(0)
        res.next=head
        pre=res
        foundDuplicated=False

        while head and head.next:
            # 连续的两个节点的值相等
            while head and head.next and head.val==head.next.val:
                head=head.next
                foundDuplicated=True
            # 更新next的指向
            if foundDuplicated:
                pre.next=head.next
                foundDuplicated=False
            # 更新节点的指向
            else:
                pre=head
            head=head.next
        return res.next

