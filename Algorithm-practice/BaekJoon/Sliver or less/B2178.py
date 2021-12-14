"""
별로 어렵지 않게 bfs 풀었다.
"""

from collections import deque

n, m = map(int, input().split())
table = [input() for _ in range(n)]
is_visited = [[False] * m for _ in range(n)]

# 상, 하 좌, 우
move_x = [-1, 1, 0, 0]
move_y = [0, 0, -1, 1]

q = deque([[0, 0, 1]])
while True:
    row, col, count = q.popleft()

    if row == n - 1 and col == m - 1:
        print(count)
        break

    tmp_count = count + 1
    for idx in range(4):
        tmp_row = row + move_x[idx]
        tmp_col = col + move_y[idx]


        if 0 <= tmp_row < n and 0 <= tmp_col < m and is_visited[tmp_row][tmp_col] is False and table[tmp_row][tmp_col] == '1':
            q.append([tmp_row, tmp_col, tmp_count])
            is_visited[tmp_row][tmp_col] = True