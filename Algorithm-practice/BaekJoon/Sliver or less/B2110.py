#!/usr/bin/python

# 핵심은 특정 거리보다 멀리 떨어진 지점의 '개수'를 구한다는 것이다.
# 이때, 특정 거리를 이분 탐색으로 구한다.

n, c = map(int, input().split())
house_position = sorted([int(input()) for _ in range(n)])
distance_low = 1
distance_high = house_position[-1]

answer = 0

while distance_low <= distance_high:
    distance = (distance_high+distance_low) // 2

    house_left = house_position[0]
    count = 1

    for i in range(1, n):
        house_right = house_position[i]

        if house_right - house_left >= distance:
            count += 1
            house_left = house_right

    if count >= c:
        answer = distance
        distance_low = distance + 1
    else:
        distance_high = distance - 1

print(answer)