import heapq

"""
if cost.get((cur_node, cur_state), None):
    continue

cost[(cur_node, cur_state)] = cur_cost

해당 부분은 큐에서 빼내올 때 수행하는 것과,
큐에 넣을 때 수행하는 것에서 문제가 있었다.

결과는 큐에서 빼내올 때 수행하는 것이 정답이었다.

왜냐하면 큐에 넣을 때, cost 값이 가장 작은 값을 넣어 줬는지 확인하지 못하기 때문이다.
"""


def dijkstra(n, start, end, adj, traps):
    INF = 1e9
    cost = {(start, 0): 0}
    h = []  # [node cost, node, trap state]

    start_state = 0
    if start in traps:
        start_state = 1 << traps[start]
    
    heapq.heappush(h, (cost[(start, 0)], start, start_state))
    while h:
        # 큐에 있는 원소 중 비용이 가장 적은 경로를 가져온다.
        cur_cost, cur_node, cur_state = heapq.heappop(h)

        # 우선순위 큐로 인해 만약 현재 노드가 목적지라면
        # 현재 비용이 최소이다.
        if cur_node == end:
            ans = cur_cost
            break


        # 이전에 같은 상태의 같은 노드에 방문한 적이 있다면 pass
        # 우선순위 큐로 인해 cost가 더 크기 때문이다.
        if cost.get((cur_node, cur_state), None):
            continue

        cost[(cur_node, cur_state)] = cur_cost

        is_reverse = False
        if cur_node in traps and (cur_state & (1 << traps[cur_node])):
            # 현재 노드가 함정이고 on 상태이면 reverse는 Ture가 된다.
            is_reverse = not is_reverse

        for tmp_nxt_node, tmp_nxt_cost, is_backward in adj[cur_node]:
            # 현재 노드와 순방향/역방향으로 연결된 인접 노드를 탐색.

            tmp_nxt_state = cur_state
            tmp_is_reverse = is_reverse

            if tmp_nxt_node in traps:
                idx_trap = traps[tmp_nxt_node]
                tmp_nxt_state ^= 1 << idx_trap

                if cur_state & (1 << traps[tmp_nxt_node]):
                    # 현재 상태에서 다음에 방문할 노드가 트랩이고
                    # 이전에 방문한 적이 있어 on인 상태
                    tmp_is_reverse = not tmp_is_reverse
                    

            if is_backward == tmp_is_reverse:
                # 현재 노드와 진행할 노드 사이의 순방향/역방향 선택.
                sum_cost = cur_cost+tmp_nxt_cost
                # 다음 상태 우선순위 큐에 넣기
                heapq.heappush(h, (sum_cost, tmp_nxt_node, tmp_nxt_state))

    return ans


def init_adj(n, start, end, roads, traps):
    for i in range(len(roads)):
        roads[i] = list(map(int, roads[i]))

    adj = [[] for _ in range(n+1)]
    for road in roads:
        src = road[0]
        dst = road[1]
        cost = road[2]

        adj[src].append([dst, cost, False])
        adj[dst].append([src, cost, True])

    traps_idx = {v: i for i, v in enumerate(traps)}

    return adj, traps_idx


def solution(n, start, end, roads, traps):

    adj, traps_idx = init_adj(n, start, end, roads, traps)
    ans = dijkstra(n, start, end, adj, traps_idx)

    return ans


# print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
print(solution(4, 3, 4, [[1, 4, 1], [1, 3, 1], [1, 2, 1], [3, 2, 1],], [1, 3, 4]))
