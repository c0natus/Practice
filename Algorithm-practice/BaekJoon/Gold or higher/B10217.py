"""
1. hours[n]이 INF가 아닐 때 while문을 멈춰도 된다. 
- 우선순위 큐로 hours[n]이 업데이트 될 때 최저 시간을 보장하기 때문이다.

2. 이를 위해 heap에서 뺄 때 정보 업데이트한다. --> 잘못된 생각
- while hours[n] == INF and heap: 으로 설정 한다. 

3. heap에 정보 추가할 조건
3.1. 현재까지 비용이 최대 비용 이하이다.
3.2. 같은 vertex로 갈 때 이전 path보다 현재 path 비용이 더 적게 들 때

3. 2번 처럼 heap에서 뺄 때 정보 업데이트하면 우선순위 큐의 크기가 너무 많아진다.
- 왜냐하면 3 -> 4인 비행기의 비용이 10 이고 시간이 10인 정보가 큐에 있을 때, 
- 3-> 4인 비행기의 비용이 11이고 시간이 11인 정보는 필요가 없지만 큐에 들어가게 된다.
- 따라서 큐에 넣을 때 정보를 업데이트한다. 그리고 큐에서 뺄 때 cur_node가 n이면 while문을 멈춘다.

4. 특정한 비행기로 이동할 수 없다고 해서 그 정보를 버리면 안 된다.
- 처음에 costs = [INF] * (n+1)로 주고 
- if next_cost <= money and costs[next_vertex] > next_cost: 일 때 큐에 넣었다.
- 이러면 아래와 같은 상황에서 필요 없는 정보를 큐에 넣게 되어 메모리 초과가 일어난다.
- 3 -> 4인 비행기의 비용이 10이고 시간이 10인 것을 통해 갈 수 없어서,
- 3 -> 4인 비행기의 비용이 9이고 시간이 15인 것을 통해 가도록 정보가 업데이트 됐을 때,
- 3 -> 4인 비행기의 비용이 11이고 시간이 11인 것은 추가될 필요가 없지만, 
- 이전 정보(비용 10, 시간 10)를 모르기 때문에 추가된다.
- 따라서 hours[vertex][cost] = next_hour를 통해 기록을 해서 메모리를 절약하자.
- 이때, hours[next_vertex][next_cost ~ money + 1] 중에서 next_hour보다 작은 것이 나올 때까지
- 모든 cost노드들을 next_hour로 업데이트 한다. 
- 이는 cost가 높고 hours가 높은 것은 큐에 추가하지 않기 위함이다. 
"""

import sys
import heapq

input = sys.stdin.readline

def djikstar(n, money):
    INF = 1000010
    hours = [[INF] * (money + 1) for _ in range(n + 1)]

    heap = []
    heapq.heappush(heap, (0, 1, 0))
    hours[1][0] = 0

    while heap:
        cur_hour, cur_vertex, cur_cost = heapq.heappop(heap)

        if cur_vertex == n: return cur_hour

        for next_vertex, add_cost, add_hour in adj[cur_vertex]:
            next_hour = cur_hour + add_hour
            next_cost = cur_cost + add_cost

            if next_cost <= money and next_hour < hours[next_vertex][next_cost]:
                heapq.heappush(heap, (next_hour, next_vertex, next_cost))

                # 메모리를 줄이기 위한 구간
                for cost in range(next_cost, money + 1):
                    if hours[next_vertex][cost] <= next_hour:
                        break
                    hours[next_vertex][cost] = next_hour

    return "Poor KCM"


for _ in range(int(input())):
    n, money, k = map(int, input().split())
    incheon = 1
    LA = n

    adj = [[] for _ in range(n + 1)]

    for _ in range(k):
        src, dst, cost, hour = map(int, input().split())
        adj[src].append([dst, cost, hour])

    print(djikstar(n, money))