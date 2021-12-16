"""
기본적인 다익스트라 문제이다.
다익스트라는 다이나믹 프로그래밍을 활용한 대표적인 최단 경로 탐색 알고리즘이다.
하나의 최단 거리를 구할 때 그 이전까지 구했던 최단 거리 정보를 그대로 사용하기 때문이다.


다익스트라는 시작점부터 각 정점들 까지의 최단 거리를 구할 수 있다.
단 음의 간선을 포함할 수 없다.

현재 문제는 방향성을 가지지만 방향성이 없는 그래프에서도 적용 가능하다.
"""

import sys
import heapq

input = sys.stdin.readline

def djikstra(start_vertex):
    costs[start_vertex] = 0
    heap = []
    heapq.heappush(heap, (costs[start_vertex], start_vertex))

    while heap:
        cur_vertex = heapq.heappop(heap)[1]
        for adj_v_c in adj[cur_vertex]:
            adj_vertex = adj_v_c[0]
            adj_weight = adj_v_c[1]

            adj_cost = costs[cur_vertex] + adj_weight

            if adj_cost < costs[adj_vertex] or costs[adj_vertex] == -1:
                costs[adj_vertex] = adj_cost
                heapq.heappush(heap, (costs[adj_vertex], adj_vertex))


v, e = map(int, input().split())
start_vertex = int(input())
adj = [[] for _ in range(v+1)]
for _ in range(e):
    src, dst, weight = map(int, input().split())
    adj[src].append([dst, weight])

costs = [-1] * (v+1)
costs[start_vertex] = 0

djikstra(start_vertex)

for idx in range(1, v+1):
    print('INF') if costs[idx] == -1 else print(costs[idx])