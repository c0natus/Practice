import sys
import heapq

input = sys.stdin.readline

def dijkstra(start, INF):
    heapq.heappush(h, (arr_cost[start], start))

    while h:
        cur = heapq.heappop(h)
        cur_cost = cur[0]
        cur_v = cur[1]

        for adj_node in adj[cur_v]:
            adj_v = adj_node[0]
            adj_cost = adj_node[1]
            tmp_route_cost = arr_cost[cur_v] + adj_cost
            if arr_cost[adj_v] > tmp_route_cost:
                arr_cost[adj_v] = tmp_route_cost
                heapq.heappush(h, (arr_cost[adj_v], adj_v))


v, e = map(int, input().split())
start = int(input())
adj = [[] for _ in range(v+1)]

for _ in range(e):
    src, dst, cost = map(int, input().split())
    adj[src].append([dst,cost])

INF = 3000000
arr_cost = [INF] * (v+1)
arr_cost[start] = 0
h = []
dijkstra(start, INF)

for i in range(1,v+1):
    if arr_cost[i] == INF:
        print('INF')
    else:
        print(arr_cost[i])