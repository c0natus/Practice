from collections import deque

def bfs():
    global start_row, start_col, target_row, target_col, l

    is_visited = [[False] * l for _ in range(l)]
    q = deque()
    q.append([start_row, start_col])
    is_visited[start_row][start_col] = True
    count = 0

    while q:
        for _ in range(len(q)):
            cur_row, cur_col = q.popleft()

            if cur_row == target_row and cur_col == target_col:
                return count

            for idx in range(8):
                nxt_row = cur_row + move_row[idx] 
                nxt_col = cur_col + move_col[idx]

                if 0 <= nxt_row < l and 0 <= nxt_col < l and is_visited[nxt_row][nxt_col] is False:
                    q.append([nxt_row, nxt_col])
                    is_visited[nxt_row][nxt_col] = True
        count += 1

    return 

move_row = [-1, 1, -2, 2, -2, 2, -1, 1]
move_col = [-2, -2, -1, -1, 1, 1, 2, 2]

for _ in range(int(input())):
    
    l = int(input())
    start_row, start_col = map(int, input().split())
    target_row, target_col = map(int, input().split())

    print(bfs())