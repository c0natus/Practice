n, k = map(int, input().split())
coin = [0] * n

for i in range(n):
    coin[i] = int(input())


# dp[i] = 합이 i가 될 수 있는 경우의 수
# dp[i] = (dp[1] + dp[i-1]) + (dp[2] + dp[i-2]) + ...
dp = [0] * (k+1)
dp[0] = 1

for i in range(n):
    for j in range(coin[i], k+1):
        dp[j] += dp[j-coin[i]]

print(dp[k])