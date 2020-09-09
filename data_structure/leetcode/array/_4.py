# URL: https://leetcode.com/problems/median-of-two-sorted-arrays/

# Main idea: 给定两个分别大小为m和n的排序数组nums1和nums2，返回两个排序数组的中位数。
# 要求：时间复杂度为O(log(m+n))

# 解题思想：
# （1)当不要求的时间复杂度时，我们可以将两个有序的数组进行合并，然后取出中间的数， 此时的时间复杂度为O（nlogn）
# （2）暗示题目的follow up的时间的复杂度进行解题，分析过来，时间复杂度要求为O(log(m+n))，分析这个时间复杂度，
# 同时考虑到是已经排好序的数组，那么就是位置确定，拿题目的样例来进行分析 nums1 = [1,2], nums2 = [3,4],合并完成后，
# merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.单独的拆开来看，需要的结果是第一个数组的最后一个位置
# 和第二个数组的第一个位置，那么这个位置是怎么得到的呢？因为总共是存在4个数的，就是第2个数和第3个数

class Solution:
    def findMedianSortedArraysNotFollowUp(self, nums1: list, nums2: list) -> float:
        """
        不要求时间复杂度的做法,直接将，两个数组进行合并
        :param nums1:
        :param nums2:
        :return:
        """
        nums = nums1 + nums2
        nums = sorted(nums)
        return nums[len(nums) // 2] if len(nums) % 2 == 1 else (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2

    def findMedianSortedArraysFollowUp(self, nums1: list, nums2: list) -> float:
        """
        按照题目时间复杂度的要求进行解题
        :param nums1:
        :param nums2:
        :return:
        """
        l = len(nums1) + len(nums2)
        #  长度为奇数
        if l % 2 == 1:
            return self.kth(nums1, nums2, l // 2)
        # 长度为偶数
        else:
            return (self.kth(nums1, nums2, l // 2) + self.kth(nums1, nums2, l // 2 - 1)) / 2.

    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a) // 2, len(b) // 2
        ma, mb = a[ia], b[ib]

        # when k is bigger than the sum of a and b's median indices
        if ia + ib < k:
            # if a's median is bigger than b's, b's first half doesn't include k
            if ma > mb:
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.kth(a[ia + 1:], b, k - ia - 1)
        # when k is smaller than the sum of a and b's indices
        else:
            # if a's median is bigger than b's, a's second half doesn't include k
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)
