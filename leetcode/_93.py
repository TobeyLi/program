# url:https://leetcode.com/problems/restore-ip-addresses/

# Main idea:给定一个字符串，字符串中全都是数字，要求返回这个字符串可能组成的有效的ip地址序列，每个划分的序列是在0～255之间
# 如Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]

# 解题思路：对于这种找到所有有效的字符串事，首先考虑到的事采用递归（DFS）方式来进行遍历，
# 遍历条件为：若是三位数，那么三位数必须是小于等于255，且这个三位数是合法的（如011类似的是不合法的）
# 我们用k来表示当前还需要分的段数，如果k = 0，则表示三个点已经加入完成，四段已经形成，若这时字符串刚好为空，
# 则将当前分好的结果保存。若k != 0, 则对于每一段，我们分别用一位，两位，三位来尝试，分别判断其合不合法，如果合法，
# 则调用递归继续分剩下的字符串，最终和求出所有合法组合


class Solution:
    def restoreIpAddresses(self, s: str):
        res = []
        self.__dfs(s, [], res)
        return res

    def __dfs(self, s, path, res):
        # 剪枝操作，检查一下所有的字符串的长度是不是能满足在最多4个3位数字组成
        if len(s) > (4 - len(path)) * 3:
            return
        if not s and len(path) == 4:
            res.append('.'.join(path))
            return
        for i in range(min(3, len(s))):
            curr = s[:i + 1]
            # 判断生成的字符是否符合条件
            if (curr[0] == '0' and len(curr) >= 2) or int(curr) > 255:
                continue
            self.__dfs(s[i + 1:], path + [s[:i + 1]], res)
if __name__ == '__main__':
    s="25525511135"
    solution=Solution()
    solution.restoreIpAddresses(s)