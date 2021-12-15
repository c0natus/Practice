"""
dfs로 풀면 메모리 초과가 나온다.
bfs로 하자.

bfs로 할 때, is_visited를 조심하자.
같은 노드에 도착했어도 벽을 깰 수 있는 경우와 없는 경우가 있다.

11% 반례
8 8
01000100
01010100
01010100
01010100
01010100
01010100
01010100
00010100
답: 29

35% 반례
8 8
00110000
00110010
00110010
00110010
00110010
00100010
00110010
00110010
답: 25


100% 반례
1 1
0
답: 1
"""

from collections import deque

def go(cur_row, cur_col, breakable):

    if boards[cur_row][cur_col] == '0' and is_visited[cur_row][cur_col][breakable] == False:
        if breakable:
            is_visited[cur_row][cur_col][0] = True
        is_visited[cur_row][cur_col][breakable] = True
        return True, breakable
    elif boards[cur_row][cur_col] == '1' and breakable:
            is_visited[cur_row][cur_col][0] = True
            return True, 0
    
    return False, breakable


def bfs():
    global row, col

    if row == 1 and col == 1:
        return 1

    q = deque([[0, 0, 1]])

    count = 1

    while q:
        tmp_q = deque()

        for cur_row, cur_col, breakable in q:
            if cur_row == row - 1 and cur_col == col - 1:
                return count
            # 상
            if cur_row > 0:
                nxt_row = cur_row - 1
                can_go, tmp_breakable = go(nxt_row, cur_col, breakable)
                if can_go:
                    tmp_q.append([nxt_row, cur_col, tmp_breakable])
            # 하
            if cur_row < row - 1:
                nxt_row = cur_row + 1
                can_go, tmp_breakable = go(nxt_row, cur_col, breakable)
                if can_go:
                    tmp_q.append([nxt_row, cur_col, tmp_breakable])
            # 좌
            if cur_col > 0:
                nxt_col = cur_col - 1
                can_go, tmp_breakable = go(cur_row, nxt_col, breakable)
                if can_go:
                    tmp_q.append([cur_row, nxt_col, tmp_breakable])
            # 우
            if cur_col < col - 1:
                nxt_col = cur_col + 1
                can_go, tmp_breakable = go(cur_row, nxt_col, breakable)
                if can_go:
                    tmp_q.append([cur_row, nxt_col, tmp_breakable])
        
        q = tmp_q        
        count += 1

    return -1


row, col = map(int, input().split())
boards = [input() for _ in range(row)]
is_visited = [[[False] * 2 for _ in range(col)] for _ in range(row)]
is_visited[0][0][1] = True
print(bfs())