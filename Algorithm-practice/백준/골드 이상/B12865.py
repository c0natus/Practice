#!/usr/bin/python3

"""
reference: https://chanhuiseok.github.io/posts/improve-6/
"""

def knapsack(n, W, w, p):
    # memo[i][j]에는 memo[i-1][j]의 값과 memo[i-1][j-w[i]]+p[i]의 값 중 더 큰 값이 들어가게 된다.
    # 즉, i번째 물건을 넣지 않은 경우와 넣은 경우 중 가치가 더 큰 값을 memo[i][j]에 저장한다.
    # 이때 가방의 용량인 j가 물건의 무게 w[i]보다 작을 때는 당연히 위의 과정이 필요없이 memo[i][j]에는 memo[i-1][j]의 값이 저장된다.
    for tn in range(1, n + 1):
        for tw in range(1, W + 1):
            if tw >= w[tn]:
                memo[tn][tw] = max(memo[tn - 1][tw], memo[tn - 1][tw - w[tn]] + p[tn])
            else:
                memo[tn][tw] = memo[tn - 1][tw]

    return memo[n][W]


if __name__ == '__main__':
    # n은 물품의 수, W는 담을 수 있는 최대 무게
    n, W = map(int, input().split())
    # w[i]는 물품의 무게, p[i]는 물건의 가치
    w = [0] * (n + 1)
    p = [0] * (n + 1)

    # memo[i][j] = 처음부터 i번째까지의 물건을 살펴보고, 배낭의 용량이 j였을 때 배낭에 들어간 물건의 가치합의 최대값.
    memo = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        w[i], p[i] = map(int, input().split())

    print(knapsack(n, W, w, p))