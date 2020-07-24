#url:https://leetcode.com/problems/minimum-window-substring/

# Main idea:
# Obviously,we should use the "Sliding window method",we may use a dict to count how many different
# alphets in t,and we traverse s.Method step:
# 一、首先遍历t，对于t中的每个字符，统计其出现的次数，记录成字典t_dict
# 二、遍历s，设置计数器cnt，若当前遍历的第i个字母出现同时出现在t中，那么t_dict中对应字符的值会减去1，若这个字符的值
# 仍然是大于0的，那么计数器cnt+1
# 三、当cnt等于t字符串的长度时，开始循环，记录一个字符串并且开始更新最小字符串。然后将窗口的左边界右移，看是否是
# 仍然包含t

import collections
class Solution:
    def minWindow(self, s, t):
        need = collections.Counter(t)
        missing = len(t)
        start, end = 0, 0
        left = 0
        for right, char in enumerate(s, 1):
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                need[s[left]] += 1
                missing += 1
                # 处在起始位置或者字字符串已经小于当前记录的字串
                if end == 0 or right-left < end-start:
                    start, end = left, right
                left += 1
        return s[start:end]

if __name__ == '__main__':
    s=Solution()
    S = "ADOBECODEBANC"
    T = "ABC"
    s.minWindow(S,T)

