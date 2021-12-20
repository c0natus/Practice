"""
처음에는 1부터 n까지 수를 증가하며 -1, // 2, // 3을 비교하며 제일 작은 count에 1을 더해줬다.

훨씬 더 빠른 코드를 봐서 그것을 참고하여 풀어보았다.
reference: https://www.acmicpc.net/source/36468391

해당 풀이는 //3, //2, -1을 queue에 넣고 하나씩 꺼내 올 때 그 값이 1이면 while문을 그만둔다.
왜냐하면 1이 나왔을 때 그것이 가장 최소 횟수로 찾은 것이기 때문이다.
또한, nums[//3, //3, -1]이 0일 때, 즉 이전에 방문한 적이 없을 때 큐에 넣어줘서 중복을 피한다.
"""
#!/usr/bin/python
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
nums = [0] * (n+1)
order = deque()
order.append(n)

while order:
    cur = order.popleft()
    if cur == 1:
        break
    
    if cur % 3 == 0 and nums[cur // 3] == 0:
        order.append(cur // 3)
        nums[cur // 3] = cur

    if cur % 2 == 0 and nums[cur // 2] == 0:
        order.append(cur // 2)
        nums[cur // 2] = cur

    if nums[cur - 1] == 0:
        order.append(cur - 1)
        nums[cur - 1] = cur

path = []
cur, cnt = 1, 0
while cur < n:
    path.append(cur)
    cur = nums[cur]
    cnt += 1

path.append(n)

print(cnt)
print(*path[::-1])