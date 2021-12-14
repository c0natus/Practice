# Bottom-up 방식으로 풀면 통과가 된다.
# 대신 top-down 방식보다 시간이 좀 더 오래 걸린다.

if __name__ == '__main__':
    n = int(input())
    if n == 1:
        print(0)
    elif n == 2:
        print(1)
    elif n == 3:
        print(1)
    else:
        dp = [1e6] * (n+1)

        dp[1] = 0
        dp[2] = 1
        dp[3] = 1

        for i in range(4, n+1):
            if i % 3 == 0:
                dp[i] = min(dp[i], dp[i//3] + 1)
            if i % 2 == 0:
                dp[i] = min(dp[i], dp[i//2] + 1)
            dp[i] = min(dp[i], dp[i-1] + 1)

        print(dp[n])

# Top-down 방식으로 진행하니 메모리 초과가 나왔다. 함수를 call하는 부분에서 많은 recursion이 일어난 것 때문이다.
#  def dp(n):
#     if n == 1:
#         return 0

#     if memo[n] != 0:
#         return memo[n]
#     else:
#         min_ = 1e6 // 2

#         if n % 3 == 0:
#             min_ = min(min_, dp(n//3) + 1)
#         if n % 2 == 0:
#             min_ = min(min_, dp(n//2) +1)
#         min_ = min(min_, dp(n-1)+1)

#         memo[n] = min_
#         return memo[n]


# if __name__ == '__main__':
#     n = int(input())
#     memo = [0] * (n+1)
#     print(dp(n))
