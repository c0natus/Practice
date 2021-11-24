def mul_matrix(m1,m2, n):
    ret = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ret[i][j] += m1[i][k] * m2[k][j]
            ret[i][j] %= 1000
    
    return ret



def pow_matrix(m, b, n):
    if b == 1:
        for i in range(n):
            for j in range(n):
                m[i][j] %= 1000
        return m
    else:
        if b % 2 == 1:
            return mul_matrix(m, pow_matrix(mul_matrix(m, m, n), (b-1)//2, n), n)
        else:
            return pow_matrix(mul_matrix(m, m, n), b//2, n)

def print_matrix(m, n):
    for i in range(n):
        for j in range(n):
            print(m[i][j], end=' ')
        print()


n,b = map(int, input().split())
arr = [None] * n
for i in range(n):
    arr[i] = list(map(int, input().split()))

print_matrix(pow_matrix(arr,b,n), n)