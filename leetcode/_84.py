# url:https://leetcode.com/problems/largest-rectangle-in-histogram/

# Main idea:给出一个list，里面的每个元素代表长方形的高（宽固定为1），在直方图中找到最大矩形的面积。

# 主要的解答：求解最值的方式我们一般都回去考虑采用动态规划的方式去做，主要是找到状态转移方程

class Solution:
    def largestRectangleArea_dp(self, heights):
        """
        采用dp的方式去做，比较复杂
        :param heights:
        :return:
        """
        l = len(heights)
        if heights is None or l == 0:
            return 0
        min_height = [[None for _ in range(l)] for _ in range(l)]
        max_area = 0
        for i in range(l):
            min_height[i][i] = heights[i]
            max_area = max(max_area, heights[i])
        for i in range(l - 2, -1, -1):
            k = l - i - 1
            for j in range(i + 1):
                min_height[j][k] = min(min_height[j + 1][k], min_height[j][k - 1])
                max_area = max(max_area, (l - i) * min_height[j][k])
                k += 1
        return max_area

    def largestRectangleArea_stack(self,heights):
        """
        采用递增栈来解决问题，比较简单易懂，维护栈顶元素，保持栈顶元素的值最大
        :param heights:
        :return:
        """
        res=0
        stack=[]
        # 末尾元素添加0，避免处理最后一个元素
        heights.append(0)
        for i in range(len(heights)):
            # 不满足递增栈的要求时，开始计算面积
            while len(stack)!=0 and heights[stack[-1]]>=heights[i]:
                cur=stack[-1]
                stack.pop()
                res=max(res,heights[cur]*i if len(stack)==0 else heights[cur]*(i-stack[-1]-1))
            stack.append(i)
        return res



if __name__ == '__main__':
    solution=Solution()
    nums=[2,4,5,6,2,3]
    res=solution.largestRectangleArea_stack(nums)
    print(res)