#!/usr/bin/python
# closet pair 알고리즘.

import sys
input = sys.stdin.readline

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(A,B):
    return (A.x - B.x) ** 2 + (A.y - B.y) ** 2


def divide(index_start, index_end):
    if index_end - index_start < 3:
        return findMinDistance(index_start, index_end)
    else:
        index_mid = (index_start + index_end) // 2
        distance_left = divide(index_start, index_mid)
        # 여기서 index_mid를 포함시켜 줘 setInterval의 계산량을 줄여서 시간 초과를 해결했다.
        # distance_right = divide(index_mid + 1, index_end)
        distance_right = divide(index_mid, index_end)

        return merge(index_start, index_end, index_mid, min(distance_left, distance_right))


def findMinDistance(index_start, index_end):
    answer = 2 * 200000 ** 2
    for i in range(index_start, index_end):
        for j in range(i+1, index_end+1):
            answer = min(answer, distance(coordinate[i], coordinate[j]))

    return answer
    

def merge(index_start, index_end, index_mid, distance_min):
    # 해당 문제의 핵심 부분으로 가지치기가 중요하다.
    index_left, index_right = setInterval(index_start, index_end, index_mid, distance_min)
    distance_merge = distance_min

    sort_coordinate_key_y = sorted(coordinate[index_left:index_right+1], key=lambda point:point.y)

    index_end = index_right - index_left
    for i in range(index_end):
        for j in range(i+1, index_end+1):
            if (sort_coordinate_key_y[j].y - sort_coordinate_key_y[i].y) ** 2 < distance_merge:
                distance_merge = min(distance(sort_coordinate_key_y[i], sort_coordinate_key_y[j]), distance_merge)
            else:
                break
    
    return distance_merge


def setInterval(index_start, index_end, index_mid, distance_min):
    # 여기를 잘못해 시간초과가 계속 났다.
    # divide를 할 때, mid를 포함시키지 않아 모든 점들의 x좌표를 비교했다.
    # 하지만, divide를 할 때 mid를 포함시켜 그 구간을 줄여서 시간초과를 없앴다.

    # index_left = 0
    # index_right = len(coordinate) - 1
    
    index_left = index_start
    index_right = index_end

    while (coordinate[index_mid].x - coordinate[index_left].x) ** 2 > distance_min:
        index_left += 1
    
    while (coordinate[index_right].x - coordinate[index_mid].x) ** 2 > distance_min:
        index_right -= 1

    return index_left, index_right

if __name__ == '__main__':
    n = int(input())
    coordinate = [None] * n

    for i in range(n):
        x, y = map(int, input().split())
        coordinate[i]=Point(x, y)
    
    coordinate.sort(key=lambda point:(point.x))

    answer = divide(0, n-1)
    print(answer)