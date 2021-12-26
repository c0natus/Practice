"""
해당 문제는 1208번 부분수열의 합2와 다르게 모든 무게가 양수이다.
따라서 물건들로 만들 수 있는 합이 목표 값보다 작거나 같으면,
findSubSum에서 tmp_arr에 추가한다.

그리고 1208번 처럼 Count를 사용하는 것보단, 이분 탐색을 이용한 것이 더 빠르다.
그 이유는 1208번은 딱 알맞은 값을 고르는 것이고, 현재 문제는 범위를 고르는 문제인데,
Counter를 사용하면 불필요한 범위를 반복하기 때문이다.
"""

#!/usr/bin/python
import sys
from collections import Counter

input = sys.stdin.readline

def findSubSum(sub_sum, sub_arr, c):
    for basis in sub_arr:
        tmp_arr = []
        for element in sub_sum:
            tmp_sum = element + basis
            if tmp_sum <= c:
                tmp_arr.append(tmp_sum)
        sub_sum += tmp_arr


n, c = map(int, input().split())
stuff = list(map(int, input().split()))

border = n // 2
stuff_a = stuff[:border]
stuff_b = stuff[border:]

sum_a, sum_b = [0], [0]

findSubSum(sum_a, stuff_a, c)
findSubSum(sum_b, stuff_b, c)

sum_a.sort()
sum_b.sort()

left, right = 0, len(sum_b) - 1
count = 0

while left < len(sum_a) and right >= 0:
    if sum_a[left] + sum_b[right] <= c:
        count += right + 1
        left += 1
    else:
        right -= 1

print(count)