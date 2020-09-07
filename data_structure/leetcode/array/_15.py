# URL: https://leetcode.com/problems/3sum/

# Main idea: 三数之和，给出一个list和一个target，三个数之和等于0，若存在，则返回这三个数

# 解题思想：
# （1）最直接的想法就是暴力遍历，每次遍历三个数，时间复杂度为O（n^3）；

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
