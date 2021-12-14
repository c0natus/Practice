"""
처음에 dp[i][j]: i번째 메모리까지 봤을 때, j용량을 가지기 위한 최소 cost라고 설정했다.
하지만 j의 최대 크기가 10000000이므로 메모리 초과가 나온다.

따라서 dp[i][j]: i번째 메모리까지 봤을 때, j비용으로 만들 수 있는 최대 memory라고 설정하자.
j의 최대 크기는 100이므로 메모리 초과가 나오지 않는다.
"""

n, m = map(int, input().split())
memories = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))

sum_cost = sum(costs[1:])

# dp[i][j]: i번째 메모리까지 봤을 때, j비용을 가지기 위한 최대 memory
dp = [[0] * (sum_cost + 1) for _ in range(n + 1)]

for idx in range(1, n + 1):
    for cost in range(sum_cost + 1):
        diff = cost - costs[idx]
        if diff >= 0:
            dp[idx][cost] = max(dp[idx-1][cost], dp[idx-1][diff] + memories[idx])
        else:
            dp[idx][cost] = dp[idx-1][cost]
    

for cost in range(sum_cost + 1):
    if dp[n][cost] >= m:
        print(cost)
        break