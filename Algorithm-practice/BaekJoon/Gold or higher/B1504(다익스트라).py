import sys
import heapq

input = sys.stdin.readline

def djikstra(start, end):
    global v, INF
    costs = [INF] * (v + 1)

    heap = []
    heapq.heappush(heap, (0, start))
    costs[start] = 0

    while heap:
        _, cur = heapq.heappop(heap)
        for adj, weight in adj_arr[cur]:
            adj_cost = costs[cur] + weight
            if costs[adj] > adj_cost:
                costs[adj] = adj_cost
                heapq.heappush(heap, (costs[adj], adj))

    return costs[end]


INF = 1e9
v, e = map(int, input().split())
adj_arr = [[] for _ in range(v+1)]
for _ in range(e):
    src, dst, weight = map(int, input().split())
    adj_arr[src].append([dst, weight])
    adj_arr[dst].append([src, weight])

must_visited = list(map(int, input().split()))

path_1_2 = djikstra(1, must_visited[0]) + djikstra(must_visited[0], must_visited[1]) + djikstra(must_visited[1], v)
path_2_1 = djikstra(1, must_visited[1]) + djikstra(must_visited[1], must_visited[0]) + djikstra(must_visited[0], v)
min_path = min(path_1_2, path_2_1)
print(-1) if min_path >= INF else print(min_path)