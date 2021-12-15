from collections import deque

def parsingTomatoes():
    global COL, ROW, HEIGHT
    zero_num = COL * ROW * HEIGHT
    location_one = deque()

    for h in range(HEIGHT):
        for r in range(ROW):
            for c in range(COL):
                if tomatoes[h][r][c] == 1:
                    location_one.append([h, r, c])
                    zero_num -= 1
                elif tomatoes[h][r][c] == -1:
                    zero_num -= 1
    
    return zero_num, location_one


def minDaysForRipe():
    global COL, ROW, HEIGHT, zero_num, location_one

    answer = -1

    # 상, 하, 좌, 우, 위, 아래
    move_row = [0, 0, -1, 1, 0, 0]
    move_col = [-1, 1, 0, 0, 0, 0]
    move_height = [0, 0, 0, 0, -1, 1]

    while location_one:

        tmp_q = deque()
        answer += 1

        while location_one:
            h, r, c = location_one.popleft()
            for idx in range(6):
                tmp_height = h + move_height[idx]
                tmp_row = r + move_row[idx]
                tmp_col = c + move_col[idx]

                if 0 <= tmp_height < HEIGHT and 0 <= tmp_row < ROW and 0<= tmp_col < COL:
                    if tomatoes[tmp_height][tmp_row][tmp_col] == 0:
                        tomatoes[tmp_height][tmp_row][tmp_col] = 1
                        tmp_q.append([tmp_height,tmp_row,tmp_col])
                        zero_num -= 1
            
        location_one = tmp_q

    if zero_num == 0:
        return answer
    else:
        return -1


COL, ROW, HEIGHT = map(int, input().split())
tomatoes = [[0] * ROW for _ in range(HEIGHT)]

for h in range(HEIGHT):
    for r in range(ROW):
        tomatoes[h][r] = list(map(int, input().split()))

zero_num, location_one = parsingTomatoes()

if zero_num == 0:
    answer = 0
else:
    answer = minDaysForRipe()

print(answer)