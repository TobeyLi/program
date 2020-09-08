# URL: https://leetcode.com/problems/3sum/

# Main idea: 三数之和，给出一个list和一个target，三个数之和等于0，若存在，则返回这三个数

# 解题思想：
# （1）最直接的想法就是暴力遍历，每次遍历三个数，时间复杂度为O（n^3）；
# （2）三数之和可以直接转变为两数之和的问题，即先记录一个一个数和其下标值，即转入了两数之和，
# （3）仍然借助于两数之和的思想，但是这一题并不是再返回下标，只是需要返回对应的值，那么我们可以将三数转变为两数，
#       再通过双指针法来得到最终的结果


import collections


class Solution:
    def threeSumBruteForce(self, nums: list):
        """
        暴力解法，直接判断三数之和是否存在为0的，若存在，则加入最终的res
        :param nums: 给出的list
        :return: 符合条件的数
        """
        if not nums:
            return []
        res = []
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.append([i, j, k])
        return res

    def threeSumTransfer2TwoSum(self, nums: list):
        """
        转变为两数之和的解法,这种方式解答出来的内容是下边不相同那么最终的结果也是不相同的，需要解决的是当两个list的
        值完全相同时，那么他们就是相同（而不是需要考虑下标）,这种方式会超时
        :param nums: 给出的list
        :return: 符合条件的数
        """
        if not nums:
            return []
        res = []
        numsMap = collections.defaultdict()
        for index, val in enumerate(nums):
            numsMap[val] = index
        # transfer to two sum
        for index, val in enumerate(nums):
            target = 0 - val
            temps = self.__help(nums, target)
            for temp in temps:
                if index not in temp and len(temp) > 0:
                    checkList = sorted([nums[temp[0]], nums[temp[1]], val])
                    if checkList not in res:
                        res.append(checkList)
        return res

    def __help(self, nums: list, target):
        twoSumMap = collections.defaultdict()
        for index, val in enumerate(nums):
            twoSumMap[val] = index
        # for there may be duplciates
        res = []
        for i, val in enumerate(nums):
            temp = target - val
            if temp in twoSumMap.keys() and twoSumMap[temp] != i:
                res.append([i, twoSumMap.get(temp)])
        return res

    def threeSumTwoPointer(self, nums: list):
        """
        使用双指针法来解答
        :param nums: 给出的list
        :return: 符合条件的数
        """
        res = []
        nums = sorted(nums)
        if len(nums) == 0 or nums[0] > 0 or nums[-1] < 0:
            return res
        for index in range(len(nums) - 2):
            if nums[index] > 0:
                break
            if index > 0 and nums[index - 1] == nums[index]:
                continue
            target = 0 - nums[index]
            i, j = index + 1, len(nums) - 1
            while i < j:
                if target == nums[i] + nums[j]:
                    res.append([nums[index], nums[i], nums[j]])
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1
                    i += 1
                    j -= 1
                elif nums[i] + nums[j] < target:
                    i += 1
                else:
                    j -= 1
        return res
