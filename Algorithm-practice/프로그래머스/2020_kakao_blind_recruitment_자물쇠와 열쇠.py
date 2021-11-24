from collections import deque

def makePosition(arr, size, toZero):
    position = deque()

    for row in range(size):
        for col in range(size):
            if arr[row][col] == 1-toZero:
                position.append((row,col))

    return position


def isFit(key_position, key_position_size, lock_position, lock_position_size, lock_size):
    l_row, l_col = lock_position[0]
    for i in range(key_position_size):
        k_row, k_col = key_position[i][0], key_position[i][1]
        mv_row = l_row - k_row
        mv_col = l_col - k_col

        changed_key_position = deque()

        for j in range(key_position_size):
            if i == j:
                continue
            else:
                changed_row = key_position[j][0] + mv_row
                changed_col = key_position[j][1] + mv_col

                if 0<= changed_row < lock_size and 0<= changed_col < lock_size:
                    changed_key_position.append((changed_row, changed_col))

        is_can_go = True
        for row, col in changed_key_position:
            if not (row, col) in lock_position:
                is_can_go = False
                break
        
        if not is_can_go:
            continue

        for k in range(1,lock_position_size):
            if not (lock_position[k][0], lock_position[k][1]) in changed_key_position:
                break
            else:
                if k == lock_position_size-1:
                    return True
    return False
    


def rotatePosition(key_position, key_size, position_size):
    for i in range(position_size):
        key_position[i] = (key_position[i][1], (key_size-1)-key_position[i][0])
    return key_position

def solution(key, lock):
    key_size = len(key)
    lock_size = len(lock)
    key_position = makePosition(key, key_size, 0)   
    lock_position = makePosition(lock, lock_size, 1)

    if not lock_position:
        return True

    key_position_size = len(key_position)
    lock_position_size = len(lock_position)
    for _ in range(4):
        if isFit(key_position, key_position_size, lock_position, lock_position_size, lock_size):
            return True
        else:
            key_position = rotatePosition(key_position, key_size, key_position_size)

    return False

print(solution(
    [[0, 0, 0], [1, 0, 0], [0, 1, 1]],
    [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
))