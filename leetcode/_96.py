# url:96. Unique Binary Search Trees

# 主要是计算卡特兰数，在前面的一个题目中也已经给出了解决方案

class Solution:
    def numTrees(self, n: int) -> int:
        return math.factorial(2 * n) // (math.factorial(n) * math.factorial(n)) // (n + 1)
