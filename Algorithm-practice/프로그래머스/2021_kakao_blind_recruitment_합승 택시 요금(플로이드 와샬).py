import heapq


def solution(n, s, a, b, fares):
    d = [[20000001 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        d[x][x] = 0
    for x, y, c in fares:
        d[x-1][y-1] = c
        d[y-1][x-1] = c

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if d[j][k] > d[j][i] + d[i][k]:
                    d[j][k] = d[j][i] + d[i][k]

    minv = 40000002
    for i in range(n):
        minv = min(minv, d[s-1][i]+d[i][a-1]+d[i][b-1])
    return minv


n = [6, 7, 8]
s = [4, 3, 4]
a = [6, 4, 5]
b = [2, 1, 6]
fares = [
    [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]],
    [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]],
    [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]
]

for i in range(3):
    print(solution(n[i], s[i], a[i], b[i], fares[i]))
