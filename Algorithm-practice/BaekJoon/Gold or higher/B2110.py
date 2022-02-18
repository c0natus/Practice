import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house_position = sorted([int(input()) for _ in range(n)])
distance_low = 1 # house_position[0]
distance_high = house_position[-1] - house_position[0] + 1 # house_position[-1]

answer = 0

# distance = (low+high)//2
# distance를 기준으로 distance보다 간격이 넓은 곳에만 공유기를 설치한다.
# 만약 공유기를 모두 설치한다면, distance_low를 distance+1로 높인다.
# 만약 공유기를 모두 설치할 수 없다면, distance_high의 값을 distance-1로 낮춘다.
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