import heapq


def dijkstra(cost_map, src, n, INF):
    cost = [INF] * (n+1)
    cost[src] = 0

    q = []
    heapq.heappush(q, (cost[src], src))
    while q:
        node_cost, node = heapq.heappop(q)
        for adj_node in range(1, n+1):
            if cost_map[node][adj_node] == None:
                continue
            else:
                tmp_sum = node_cost + cost_map[node][adj_node]
                if tmp_sum >= cost[adj_node]:
                    continue
                else:
                    cost[adj_node] = tmp_sum
                    heapq.heappush(q, (cost[adj_node], adj_node))

    return cost


def solution(n, s, a, b, fares):
    INF = 20000001
    cost_map = [[None] * (n+1) for _ in range(n+1)]
    for fare in fares:
        cost_map[fare[0]][fare[1]] = cost_map[fare[1]][fare[0]] = fare[2]

    diff_src = [[]] + [dijkstra(cost_map, i, n, INF) for i in range(1, n+1)]
    answer = INF
    for i in range(1, n+1):
        answer = min(diff_src[i][a] + diff_src[i][b] + diff_src[i][s], answer)

    return answer


n = [6, 7, 8]
s = [4, 3, 4]
a = [6, 4, 5]
b = [2, 1, 6]
fares = [
    [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]],
    [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]],
    [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]
]

for i in range(3):
    print(solution(n[i], s[i], a[i], b[i], fares[i]))
