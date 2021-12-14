# 크누스 최적화를 이용해 복잡도를 줄였다.
# dp를 구하는 것에서 아직 이해가 안갔지만 error가 일어나서 틀린 답이 나왔다.
# 다른 블로그를 참고하여 dp 구하는 것을 다시 하니 통과 됐다......

import sys
input = sys.stdin.readline

dp = [[0] * 501 for i in range(501)]
c = [0] * 501
knuth = [[None] * 501 for _ in range(501)]

for _ in range(int(input())):
    k = int(input())
    paper = [None] + list(map(int, input().split()))

    # dp[i][j] = i부터 j-1까지 합치는 데 걸리는 최소 시간
    # c[i] = 1부터 i까지 부분합
    for i in range(1,k+1):
        knuth[i][i] = i
        c[i] = c[i-1] + paper[i]

    for interval in range(1, k):
        for row in range(1, k - interval + 1):
            col = row + interval
            dp[row][col] = float('inf')

            for i in range(knuth[row][col-1], knuth[row+1][col]+1):

                if i == col:
                    break
                
                tmp_total_cost = dp[row][i] + dp[i+1][col] + c[col] - c[row-1]

                if dp[row][col] > tmp_total_cost:
                    knuth[row][col], dp[row][col] = i, tmp_total_cost

    print(dp[1][k])