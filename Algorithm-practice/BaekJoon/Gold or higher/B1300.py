#!/usr/bin/python

# low는 1, high는 n^2로 두어 mid보다 작은 수의 개수를 센다
# 작은 수의 개수를 구하는 것이 핵심이다.

n = int(input())
k = int(input())

low = 1
high = n ** 2

while low < high:
    mid = (low + high) // 2

    count = 0

    for i in range(1, n+1):
        count += min(mid // i, n)
    
    if k <= count:
        high = mid
    else:
        low = mid + 1

print(low)