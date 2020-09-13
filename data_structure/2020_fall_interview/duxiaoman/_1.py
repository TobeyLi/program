# 路径遍历问题，从左上到右下，存在三种状态：
#  0：代表可通行，消耗一个能量值
#  1：障碍物，不可通行
#  #：障碍物，可以掉进去，会消耗k个能量值再跳出来

# 问从左上到右下最少消耗的能量是多少

"""
test cases：
input：
3 2
0#0
0#1
000
output：
4

"""

MAX_VALUE = float('inf')


def dfs(maze, n, k):
    path_res = []
    directions = ([1, 0], [-1, 0], [0, -1], [0, 1])

    def helper(x, y, cur):
        cur_point = maze[x][y]
        # 为障碍物
        if cur_point == '1':
            return
        # 目前的路径长度+1
        elif cur_point == '0':
            cur += 1
        # 遇到陷阱，多消耗k
        else:
            cur = cur + k + 1
        # 边界
        if x == n - 1 and y == n - 1:
            path_res.append(cur)
        # dfs
        for di, dj in directions:
            next_x, next_y = x + di, y + dj
            maze[x][y] = '1'
            if 0 <= next_x < n and 0 <= next_y < n:
                helper(next_x, next_y, cur)
            maze[x][y] = cur_point

    helper(0, 0, -1)
    if not path_res:
        return 0
    else:
        return min(path_res)


if __name__ == '__main__':
    n, k = map(int, input().split())
    maze = [list(input().strip()) for _ in range(n)]

    dfs(maze, n, k)
