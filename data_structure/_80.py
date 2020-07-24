# url:https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

# Main meaning:给定一个已经排好序的list，将list中的出现3次或者3次以上的数字进行删除，使其至多出现两次，求删除之后
# 新的数组的长度，要求算法的空间复杂度为O(1)，原来的list也进行同步的改变

# Main idea：采用双指针法进行操作。从前面开始，一个快指针对所有的数字进行遍历，另外一个慢指针指向了不满足题目要求的第一个位置。
# 这样当遍历到一个新的数字而且这个新的数字和慢指针指向的前两个数字相同时，
# 把它交换到这个不满足的位置，然后两个指针同时右移即可。

import collections
class Solution:
    def removeDuplicates(self, nums):
        """
        首先不管空间复杂度，先解决掉这个问题,可以直接来使用Counter数组来计算,这种方式可以来计算数组的长度，
        但是原本的nums数组的没有发生变化，不符合条件
        :param nums:List
        :return:int
        """
        nums_dict=collections.Counter(nums)
        length=0
        for _,value in nums_dict.items():
            if value>2:
                length+=2
            else:
                length+=value
        return length

    def removeDuplicates1(self, nums):
        if len(nums) < 3:
            return len(nums)
        # 记录数字出现次数大于2的位置
        pos = 1
        for i in range(1, len(nums)-1):
            # 当前遍历的数字的前一个与后一个不相等时，说明没有连续三个相等的数字
            if nums[i-1] != nums[i+1]:
                nums[pos] = nums[i]
                pos += 1
        nums[pos] = nums[-1]
        return pos + 1


if __name__ == '__main__':
    solution=Solution()
    nums = [0,0,1,1,2,3,3]

    print(solution.removeDuplicates1(nums))