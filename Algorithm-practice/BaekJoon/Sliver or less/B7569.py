"""
minDaysForRipe()에서 move로 for문을 하는 것이 아니라
조건이 맞으면 실행하는 식으로 진행하는 것이 더 빠르다...
reference: https://www.acmicpc.net/source/32511271
"""

import sys
from collections import deque

def parsingTomatoes():
    global COL, ROW, HEIGHT
    zero_num = 0
    location_one = deque()

    for h in range(HEIGHT):
        for r in range(ROW):
            for c in range(COL):
                if tomatoes[h][r][c] == 1:
                    location_one.append([h, r, c])
                elif tomatoes[h][r][c] == 0:
                    zero_num += 1
    
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

        for h, r, c in location_one:
            if h > 0 and tomatoes[h-1][r][c] == 0:
                tomatoes[h-1][r][c] = 1
                tmp_q.append((h-1,r,c))
            if r > 0 and tomatoes[h][r-1][c] == 0:
                tomatoes[h][r-1][c] = 1
                tmp_q.append((h,r-1,c))
            if c > 0 and tomatoes[h][r][c-1] == 0:
                tomatoes[h][r][c-1] = 1
                tmp_q.append((h,r,c-1))
            if h < HEIGHT-1 and tomatoes[h+1][r][c] == 0:
                tomatoes[h+1][r][c] = 1
                tmp_q.append((h+1,r,c))
            if r < ROW-1 and tomatoes[h][r+1][c] == 0:
                tomatoes[h][r+1][c] = 1
                tmp_q.append((h,r+1,c))
            if c < COL-1 and tomatoes[h][r][c+1] == 0:
                tomatoes[h][r][c+1] = 1
                tmp_q.append((h,r,c+1))                        
        
        zero_num -= len(tmp_q)
        location_one = tmp_q

    if zero_num == 0:
        return answer
    else:
        return -1


input = sys.stdin.readline
COL, ROW, HEIGHT = map(int, input().split())
# tomatoes = list(zip(*[iter(list(map(int, ll.split())) for ll in input)] * ROW))
tomatoes = [[list(map(int, input().split())) for _ in range(ROW)] for _ in range(HEIGHT)]

zero_num, location_one = parsingTomatoes()

if zero_num == 0:
    answer = 0
else:
    answer = minDaysForRipe()

print(answer)