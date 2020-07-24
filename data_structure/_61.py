
# Rotate List
# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL

# 算法思想：可以先把所有的内容都加入到list中，再从list中每次将最后的内容加入到list前面
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
    def creatLinkedList(self,nums):
        """
        建造一个带头节点的单链表
        :param nums:
        :return:
        """
        head=tmp=ListNode(0)
        for num in nums:
            s=ListNode(num)
            tmp.next=s
            tmp=s
        return head

class Solution:
    def rotateRight(self, head, k):
        """
        直接这样做的话，假设k比较大，但是链表比较短的情况下，这种会耗费大量的时间，那么我们是不是可以对于k进行处理,进行一个取余操作
        :param head:
        :param k:
        :return:
        """
        nums=list()
        tmp=head
        while tmp:
            nums.append(tmp.val)
            tmp=tmp.next
        if len(nums)==0:
            return None
        k=k%len(nums)
        while k>0:
            num=nums.pop(len(nums)-1)
            nums.insert(0,num)
            k-=1
        # 建立链表
        head=tmp=ListNode(0)
        for num in nums:
            s=ListNode(num)
            tmp.next=s
            tmp=s
        return head.next

if __name__ == '__main__':
    s=ListNode(0)
    nums=[1,2,3,4,5]
    head=s.creatLinkedList(nums)
    tmp=head.next
    while tmp!=None:
        print(tmp.val)
        tmp=tmp.next
    solution=Solution()

