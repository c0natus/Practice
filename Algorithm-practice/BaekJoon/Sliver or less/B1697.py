from collections import deque

def bfs(n, k):
    if n == k:
        return 0
        
    is_visited[n] = True
    q = deque([n])
    sec = 0

    is_hit = False

    while q:
        tmp_q = deque()
        sec += 1

        while q:
            position = q.popleft()

            next_pos = position - 1
            if next_pos == k:
                is_hit = True
                break
            if next_pos >= 0 and next_pos <= 100000 and is_visited[next_pos] is False:
                is_visited[next_pos] = True
                tmp_q.append(next_pos)
            
            next_pos = position + 1
            if next_pos == k:
                is_hit = True
                break
            if next_pos >= 0 and next_pos <= 100000 and is_visited[next_pos] is False:
                is_visited[next_pos] = True
                tmp_q.append(next_pos)
            
            next_pos = position * 2
            if next_pos == k:
                is_hit = True
                break
            if next_pos >= 0 and next_pos <= 100000 and is_visited[next_pos] is False:
                is_visited[next_pos] = True
                tmp_q.append(next_pos)
        
        if is_hit:
            break
        q = tmp_q

    return sec

INF = 100005
is_visited = [False] * INF
print(bfs(*map(int, input().split())))