"""
g 또는 h가 target인 경우를 놓쳤다.
g, h를 방문하지만 g-h 간선을 가지 않는 부분을 놓쳤다.
True in [1]은 True이다...

특정지점까지 최단거리 경로가 두개 이상인 경우, 다잌스트라로 구한 최단 경로는 여러개의 최단 경로 중 하나이다.

예로들어
4 4 1
1 3 4
1 2 1
2 3 1
2 4 2
3 4 1
4
일 때, 답은 4지만 답을 출력하지 않을 때도 있다.
입력 순서에 따라 인접 리스트가 만들어지는 순서가 달라지고 힙에 들어가는 순서가 달리지기 때문이다.

따라서 'if lengths[adj_node] > adj_length:'을 'if lengths[adj_node] >= adj_length:'로 바꾼다.
그리고 힙에 있는 내용이 전부 나오므로 최단 거리가 아닌데 힙에서 pop 됐다는 것만으로 'T'를 추가하면 안 된다.
50번 줄에 lengths[cur_node] >= cur_length 조건을 추가해줘야 한다.!!!!!!!
예로 들어
1
7 11 2
4 6 4
1 6 4
6 7 1
5 7 2
1 2 1
2 3 1
3 4 1
4 5 1
3 5 2
4 6 8
5 6 1
2 4 2
6
5
일 때, 답은 없다.
위에 것때문에 오래 걸림 ㅠㅠ

이러면 중복이 쓸데없이 방문해야 하는 경우가 많아진다...
따라서 방문한 기록으로 풀면 안 되고, 정점들 까지의 최단 거리로 비교해야 한다.
B1504처럼 해결해도 되지만 모든 간선마다 2배를 해주고 반드시 지나야하는 간선은 2배 -1로 주어 다익스트라를 한번만 실행한다.
이럴 경우 최단 거리가 여러 개일 경우, 반드시 지나야하는 간선을 지나면 다른 경로보다 비용이 적어지기 때문에 때문에 가능하다.
그래서 목적지 중 최단 거리가 홀수인 경우 정답으로 출력한다.
"""

import sys
from collections import deque
import heapq

input = sys.stdin.readline
INF = int(2e9)

def djikstra_routes(start, vertices):

    lengths = [INF] * (vertices + 1)
    lengths[start] = 0
    routes = [[] for _ in range(vertices + 1)]

    heap = []
    heapq.heappush(heap, (lengths[start], start, start))

    while heap:
        cur_length, cur_node, prev_node = heapq.heappop(heap)
        if 'T' in routes[cur_node]:
            continue
        elif lengths[cur_node] >= cur_length and ('T' in routes[prev_node] or [cur_node, prev_node] in [[g, h], [h, g]]):
            routes[cur_node].append('T')

        for adj_node, between_length in adj[cur_node]:
            adj_length = between_length + lengths[cur_node]
            if lengths[adj_node] >= adj_length:
                lengths[adj_node] = adj_length
                heapq.heappush(heap, (lengths[adj_node], adj_node, cur_node))

    return routes
    
for _ in range(int(input())):
    # intersection, roads, destinations
    vertices, edges, target_num = map(int, input().split())
    # start, g, h
    start_intersection, g, h = map(int, input().split())

    adj = [[] for _ in range(vertices+1)]

    # m lines with intersection a, b and length d
    for _ in range(edges):
        vertex_a, vertex_b, length_road = map(int, input().split())
        adj[vertex_a].append([vertex_b, length_road])
        adj[vertex_b].append([vertex_a, length_road])

        if [vertex_a, vertex_b] in [[g, h], [h,g ]]:
            g_h_length = length_road

    # t lines
    targets = [0] * target_num
    for idx in range(target_num):
        targets[idx] = int(input())
    targets.sort()
    
    direct_routes = djikstra_routes(start_intersection, vertices)

    for target in targets:
        if 'T' in direct_routes[target]:
            print(target, end=' ')