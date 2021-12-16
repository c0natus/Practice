"""
sys 모듈을 사용하지 않으면 시간 초과가 나온다.
"""

from collections import deque
import sys

input = sys.stdin.readline

def bfs():
    global v
    
    vertex_set = [1] + [0] * v

    for vertex in range(1, v + 1):
        if vertex_set[vertex] == 0:
            q = deque()
            q.append(vertex)
            vertex_set[vertex] = 1

            while q:
                for _ in range(len(q)):
                    cur_vertex = q.popleft()
                    for adj_vertex in adj[cur_vertex]:
                        if vertex_set[adj_vertex] == 0:
                            vertex_set[adj_vertex] = vertex_set[cur_vertex] * -1
                            q.append(adj_vertex)
                        else:
                            if vertex_set[adj_vertex] == vertex_set[cur_vertex]:
                                return 'NO'
    
    return 'YES'

for _ in range(int(input())):
    v, e = map(int, input().split())
    adj = [[] for _ in range(v+1)]

    for _ in range(e):
        vertex1, vertex2 = map(int, input().split())
        adj[vertex1].append(vertex2)
        adj[vertex2].append(vertex1)

    print(bfs())