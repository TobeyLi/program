
# 逆转链表
class ListNode:
    def __init__(self,val, next=None):
        self.val=val
        self.next=next

def reverseList(head:ListNode):
    if head is None or head.next==None:
        return head
    pre=None
    cur=head
    h=head
    while cur:
        h=cur
        temp=cur.next
        cur.next=pre
        pre=cur
        cur=temp
    return h
