# 找到最长的路径的个数 https://leetcode.com/problems/number-of-longest-increasing-subsequence/
# leetcode 673
def findLongestSequenceNumber(nums):
    # 初始化
    dp, res = [[1, 1] for _ in range(len(nums))], 1
    for i in range(1, len(nums)):
        cur, cnt = 1, 0
        for j in range(i):
            if nums[j] < nums[i]:
                cur = max(cur, dp[j][0]+1)
        for j in range(i):
            if dp[j][0] == cur - 1 and nums[j] < nums[i]:
                cnt += dp[j][1]
        dp[i] = [cur, max(cnt, dp[i][1])]
        res = max(res, cur)
    # 统计最终的结果
    return sum([val[1] for val in dp if val[0] == res])


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    print(findLongestSequenceNumber(nums))