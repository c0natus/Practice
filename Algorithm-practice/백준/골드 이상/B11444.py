def pow_matrix(matrix, n):
    global p
    if n == 1:
        return matrix
    else:
        if n % 2 == 1:
            return mul_matrix(matrix, pow_matrix(mul_matrix(matrix, matrix), n//2))
        else:
            return pow_matrix(mul_matrix(matrix, matrix), n//2)

def mul_matrix(m1, m2):
    global p
    ret = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                ret[i][j] += m1[i][k] * m2[k][j]
                ret[i][j] %= p
    return ret


def fibo(n):
    global p
    matrix = pow_matrix([[1, 1], [1, 0]], n-1)

    return matrix[0][0]


n = int(input())
p = 1000000007
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    print(fibo(n))