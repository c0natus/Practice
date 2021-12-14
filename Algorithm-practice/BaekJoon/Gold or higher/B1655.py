#!/usr/bin/python

import heapq
import sys
input = sys.stdin.readline

n = int(input())

# 최대 힙과 최소 힙을 잘 적용하면 해결되는 문제이다.
# 가운데 숫자를 찾기 위해서 아주 잘 적용해야 한다.

max_q = []
min_q = []
for _ in range(n):
    x = int(input())

    if len(min_q) == len(max_q):
        heapq.heappush(max_q, -x)
    else:
        heapq.heappush(min_q, x)

    if min_q and -max_q[0] > min_q[0]:
        max_value = -heapq.heappop(max_q)
        min_value = heapq.heappop(min_q)
        heapq.heappush(max_q, -min_value)
        heapq.heappush(min_q, max_value)
        
    print(-max_q[0])