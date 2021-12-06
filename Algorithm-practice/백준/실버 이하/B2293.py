n, k = map(int, input().split())
coin = [0] * n

for i in range(n):
    coin[i] = int(input())


# dp[i] = 합이 i가 될 수 있는 경우의 수
# dp[i] = (dp[1] + dp[i-1]) + (dp[2] + dp[i-2]) + ...
dp = [0] * (k+1)

dp[0] = 1

for i in range(n):
    # coin[i]로만 만들 수 있는 합의 경우의 수를 dp에 누적해서 더한다.
    for j in range(coin[i], k+1):
        # coin[i] == j일 때, 경우의 수는 1이므로 dp[0] = 1이 되어야
        dp[j] += dp[j-coin[i]]

print(dp[k])