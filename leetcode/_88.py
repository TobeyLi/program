# url:https://leetcode.com/problems/merge-sorted-array/
# Conditions:
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

# Main idea:
#  最直接的做法：直接按照python提供的函数进行sort，但是这样必须是进行部分返回值
#  不返回值，那么就是要对0值进行更新，因为都是排序的值，那么就是从后往前进行更新，将最大的值放在后面即可
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        这种类型的是，需要返回值，否则不会num1值不会进行改变，此时不符合条件
        """
        nums1=nums1[:m]
        nums1.extend(nums2)
        nums1.sort()
        return nums1

    def merge_1(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        不能返回任何值，需要对原始的num1内容进行改变，也就是把num1的0值进行更新
        """
        while m > 0 and n > 0:
            if nums1[m-1] >nums2[n-1]:
                nums1[m+n-1]=nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1]=nums2[n-1]
                n-=1
        # 处理剩下的内容,此时num2的n个元素都是小于num1中的元素
        if n>0:
            nums1[:n] = nums2[:n]



if __name__ == '__main__':
    solution=Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m=3
    nums2 = [2, 5, 6]
    n=3
    solution.merge_1(nums1,m,nums2,n)
    print(nums1)

