# URL: https://leetcode.com/problems/3sum-closest/

# Main idea: 三数之和和target最接近的数，给出一个list和一个target，找到和target最接近的数（这个数为list中的三数之和）

# 解题思想：
# （1）最直接的想法就是暴力遍历，每次遍历三个数，时间复杂度为O（n^3）；
# (2)采用滑动窗口的解答方式，类似于T15

class Solution:
    def threeSumClosestBruteForce(self, nums, target):
        """
        三数临近之和的暴力解法,会遇到超时的正常现象
        :param nums: 给出的list
        :param target: 目标数
        :return: 最接近的数
        """
        res = float("inf")
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    temp = nums[i] + nums[j] + nums[k]
                    if abs(temp - target) < abs(res - target):
                        res = temp
        return res

    def threeSumClosestTwoPointer(self, nums, target):
        """
        三数临近之和的滑动窗口解法
        :param nums: 给出的list
        :param target: 目标数
        :return: 最接近的数
        """
        nums = sorted(nums)
        res = float("inf")
        for t in range(len(nums)):
            i, j = t + 1, len(nums) - 1
            while i < j:
                _sum = nums[t] + nums[i] + nums[j]
                if abs(_sum - target) < abs(res - target):
                    res = _sum
                if _sum > target:
                    j -= 1
                elif _sum < target:
                    i += 1
                else:
                    return target
        return res
