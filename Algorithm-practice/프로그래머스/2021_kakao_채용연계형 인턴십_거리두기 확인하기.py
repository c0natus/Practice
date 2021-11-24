def row1_right(place, row,col):
    end = col + 3
    if end > 5:
        end = 5

    if 'P' in place[row][col+1:end] and place[row][col+1] != 'X':
        return False

    return True

def row1_left(place, row,col):
    start = col - 2
    if start < 0:
        start = 0

    if 'P' in place[row][start:col] and place[row][col-1] != 'X':
        return False

    return True    

def row2_right(place, row,col):
    if place[row+1][col+1] == 'P' and not (place[row][col+1] == 'X' and place[row+1][col] == 'X'):
        return False
    if place[row+1][col] == 'P':
        return False
    return True

def row2_left(place, row,col):
    if place[row+1][col-1] == 'P' and not (place[row][col-1] == 'X' and place[row+1][col] == 'X'):
        return False
    if place[row+1][col] == 'P':
        return False
    return True

def row3(place, row,col):
    if place[row+2][col] == 'P' and place[row+1][col] != 'X':
        return False
    return True

def solution(places):
    answer = [0] * 5
    for i in range(5):
        place = places[i]
        is_possible = True
        for j in range(5):
            seats = place[j]
            for k in range(5):
                seat = seats[k]
                if seat == 'P':
                    if k != 4:
                        is_possible = row1_right(place, j,k)
                    if k != 0 and is_possible:
                        is_possible = row1_left(place, j,k)
                    if j != 4 and k != 4 and is_possible:
                        is_possible = row2_right(place, j,k)
                    if j != 4 and k != 0 and is_possible:
                        is_possible = row2_left(place, j,k)
                    if j < 3 and is_possible:
                        is_possible = row3(place, j,k)
                if not is_possible:
                    break
            if not is_possible:
                break
        if is_possible:
            answer[i] = 1

    return answer

solution([
    ["POOOP", "PXXOX", "OPXPX", "OOXOX", "POXXP"], 
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
    ])