# url:https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Main idea:删除含有重复值的元素，使其只保留一个内容，这题和82题是一样的方式，可以采用同样的解决方式，
# 但是这题稍微简单一些，不用单独的去设计头节点，只是采用同样的遍历方式去做即可。

class ListNode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur=head

        while cur:
            while cur.next and cur.val==cur.next.val:
                cur.next=cur.next.next
            cur=cur.next
        return head