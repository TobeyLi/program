# URL:https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Main idea: 给出一个字符串，找到其最长的无重复字串

# 解题方式
# 借助两个指针，left和right，其中left指向的无重复字串的起始位置，right为遍历指针，每次遍历都更新最后的结果，
# 当没有遇到重复的字串时，那么right继续遍历，同时将遍历的元素加入到set中；若遇到重复的字符，那么找到当前遍历元素
# 的下一个（已经遍历的内容），left为当前元素下标的下一个位置，遍历结束便可以得到最终的结果

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left, right = 0, 0
        recordExist = set()
        while right < len(s):
            if s[right] not in recordExist:
                recordExist.add(s[right])
                right += 1
                res = max(res, len(recordExist))
            else:
                recordExist.remove(s[left])
                left += 1
        return res
