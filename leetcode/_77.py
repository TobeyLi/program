# url:https://leetcode.com/problems/combinations/

# Main idea:找到所有组合的方式的题目的话，我们一般需要考虑使用DFS的方式去做，
# 我们抽取第一个字符，然后从后面n-1个字符中抽出m-1个；抽取第二个字符，再从后面的n-2个字符抽出m-1个……这样循环下去。
# 因为这样的操作每次都是往后进行寻找的，所以不用考虑去重的问题。

class Solution:
    def combine(self, n, k):
        res = []
        self.helper(range(1, n + 1), k, res, [])
        return res

    def helper(self, array, k, res, path):
        if k > len(array):
            return
        if k == 0:
            res.append(path)
        else:
            for i in range(len(array)):
                self.helper(array[i + 1:], k - 1, res, path + [array[i]])

if __name__ == '__main__':
    solution=Solution()
    n = 4
    k = 2
    print(solution.combine(n,k))