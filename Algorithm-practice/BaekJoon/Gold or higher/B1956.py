"""
findMinCostPath에서 반복문을 줄여야한다.
사이클의 찾는 것이기 때문에 end를 1부터할 필요 없이 start + 1부터 해주면 된다.

그리고 python으로 하면 시간 초과가 나오므로 pypy로 제출하자.
"""
import sys

input = sys.stdin.readline

def findMinCostPath(v):
    min_path = costs[0][0] # INF

    for start in range(1, v+1):
        for end in range(start + 1, v+1):
            if start == end : continue
            sum_cost = costs[start][end] + costs[end][start]
            min_path = min(min_path, sum_cost)
    
    return - 1 if min_path == costs[0][0] else min_path
    

def floydWarshall(v):
    for through in range(1, v+1):
        for start in range(1, v+1):
            for end in range(1, v+1):
                sum_cost = costs[start][through] + costs[through][end]
                costs[start][end] = min(costs[start][end], sum_cost)

    

v, e = map(int, input().split())
INF = 1e9
costs = [[INF] * (v+1) for _ in range(v+1)]

for idx in range(1, v+1):
    costs[idx][idx] = 0

for _ in range(e):
    src, dst, cost = map(int, input().split())
    costs[src][dst] = cost


floydWarshall(v)

print(findMinCostPath(v))
