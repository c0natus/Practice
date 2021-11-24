from collections import defaultdict, deque
from itertools import permutations
import copy

# 처음에는 모든 경우의 수를 만들어 준 뒤, 움직인 횟수를 구하였다.
# 하지만 이런 경우 중복되는 값이 많아져 더 오랜 시간이 얼리게 된다.
# ex) 1a 1b 2a 2b 3a 3b와 1a 1b 2a 2b 3b 3a에서 1a ~ 2b까지는 중복이다.
#     따라서 모든 경우의 수를 만들어 주면 1a ~ 2b를 2번 계산한다.
# 따라서 백트래킹으로 중복되는 경우를 한번만 계산해주도록 하자.
# 최소 횟수를 bfs 구하는 방법은 같다.

# def makeAllCase(order, position):
#     col_size = len(order)
#     row_size = 2 ** col_size
#     ret = deque()

#     for col in range(col_size):
#         card = order[col]
#         a = position[card][0]
#         b = position[card][1]

#         if ret:
#             for i in range(len(ret)):
#                 add_list = copy.deepcopy(ret[i])
#                 ret[i].append(a)
#                 ret[i].append(b)
#                 add_list.append(b)
#                 add_list.append(a)
#                 ret.append(add_list)
#         else:
#             # ret이 비어 있을 때
#             ret.append([a,b])
#             ret.append([b,a])
    
#     return ret


def initPosition(board):
    position = defaultdict(list)
    for row in range(4):
        for col in range(4):
            if board[row][col] != 0:
                position[board[row][col]].append((row, col))
    
    return position


def canMove(row, col):
    if 0 <= row <= 3 and 0 <= col <=3:
        return True
    return False


def moveCtrl(board, row, col, direct):
    while True:
        tmp_row = row + direct[0]
        tmp_col = col + direct[1]
        if not canMove(tmp_row, tmp_col):
            return row, col
        if board[tmp_row][tmp_col] != 0:
            return tmp_row, tmp_col
        row = tmp_row
        col = tmp_col


def minMove(board, row, col, target_row, target_col):
    if (row, col) == (target_row, target_col):
        return 1
    
    move = [(0,1), (1,0), (0,-1), (-1, 0)]
    size = 4
    visited = [[False for _ in range(size)] for _ in range(size)]
    cnt_map = [[0 for _ in range(size)] for _ in range(size)]
    q = deque()
    visited[row][col] = True
    q.append((row, col))
    while q:
        init_row, init_col = q.popleft()

        for i in range(4):
            move_row, move_col = init_row + move[i][0], init_col + move[i][1]
            
            if canMove(move_row, move_col):
                if not visited[move_row][move_col]:
                    visited[move_row][move_col] = True
                    cnt_map[move_row][move_col] = cnt_map[init_row][init_col] + 1
                    if (move_row, move_col) == (target_row, target_col):
                        return cnt_map[move_row][move_col] + 1
                    else:
                        q.append((move_row, move_col))
            
            move_row, move_col = moveCtrl(board, init_row, init_col, move[i])
            if canMove(move_row, move_col):
                if not visited[move_row][move_col]:
                    visited[move_row][move_col] = True
                    cnt_map[move_row][move_col] = cnt_map[init_row][init_col] + 1
                    if (move_row, move_col) == (target_row, target_col):
                        return cnt_map[move_row][move_col] + 1
                    else:
                        q.append((move_row, move_col))

    return 1e9


def count(order, board, r, c, position, i, cnt, answer):
    if i == len(order):
        answer = min(answer, cnt)
        return answer


    card_num = order[i]

    a = position[card_num][0]
    b = position[card_num][1]

    cnt1 = minMove(board, r, c, a[0], a[1])
    cnt2 = minMove(board, a[0], a[1], b[0], b[1])

    board[a[0]][a[1]] = 0
    board[b[0]][b[1]] = 0

    answer = count(order, board, b[0], b[1], position, i+1, cnt + cnt1 + cnt2, answer)

    board[a[0]][a[1]] = card_num
    board[b[0]][b[1]] = card_num


    cnt1 = minMove(board, r, c, b[0], b[1])
    cnt2 = minMove(board, b[0], b[1], a[0], a[1])

    board[a[0]][a[1]] = 0
    board[b[0]][b[1]] = 0

    answer = count(order, board, a[0], a[1], position, i+1, cnt + cnt1 + cnt2, answer)

    board[a[0]][a[1]] = card_num
    board[b[0]][b[1]] = card_num

    return answer


def solution(board, r, c):
    position = initPosition(board)
    card_kinds = [i for i in position.keys()]

    answer = 1e9
    for order in permutations(card_kinds):
        answer = min(answer, count(order, board, r, c, position, 0, 0, answer))

    return answer


board = [
    [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],
    [[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]]
    ]
r = [1,0]
c = [0,1]

for i in range(2):
    print(solution(board[i], r[i], c[i]))