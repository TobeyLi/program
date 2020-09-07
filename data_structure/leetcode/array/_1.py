# URL: https://leetcode.com/problems/two-sum/

# Main idea: 两数之和，给出一个list和一个target，判断list中是否存在两个数之和等于target，若存在，则返回两个数
# 在list中的下标

# 解题思想：
# （1）最直接的想法就是暴力遍历，每次遍历两个数，若存在，则直接比较得到最终的结果；
# （2）借助于hashmap，因为get是常数时间复杂度，最终的时间复杂度极为O(n)

import collections


class Solution:
    def twoSumBruteForce(self, nums: list, target: int) -> list:
        """
        暴力解法，每两个数相加，和target进行判断，看是否能得到最终的结果
        :param nums: 给出的结果
        :param target: 判断的最终的结果
        :return: 结果的数据的下标
        """
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def twoSumHashMap(self, nums: list, target: int) -> list:
        """
        使用hashMap来保存下标和数字，那么判断的时候只是需要去记录减去的数是否在hashmap中
        :param nums: 给出的结果
        :param target: 判断的最终的结果
        :return: 结果的数据的下标
        """
        numsMap = collections.defaultdict()
        # construct the hashMap
        for index, value in enumerate(nums):
            numsMap[value] = index
        # traverse
        for i, val in enumerate(nums):
            temp = target - val
            if temp in numsMap.keys() and numsMap[temp] != i:
                return [i, numsMap.get(temp)]
        return []
