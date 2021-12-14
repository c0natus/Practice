def fac_mod(n, k, p):
    ret = 1
    for i in range(1, n+1):
        ret = (ret * i) % p
        if i == k:
            fac_dict['k'] = ret
        if i == n-k:
            fac_dict['n-k'] = ret
    fac_dict['n'] = ret


def euclid(n, k, p):
    s1, s2, t1, t2 = 1, 0, 0, 1
    r1, r2 = p, fac_dict['k'] * fac_dict['n-k']

    while r2 != 1:
        q = r1 // r2
        r1, r2 = r2, r1 % r2
        s1, s2 = s2, (s1 - q*s2)
        t1, t2 = t2, (t1 - q*t2)
    
    return t2 % p


n, k = map(int, input().split())
p = 1000000007
if n == 1 or n == k or k == 0:
    print(1)
else:
    fac_dict = {'n': 0, 'k': 0, 'n-k': 0}
    fac_mod(n, k, p)
    print((fac_dict['n'] * euclid(n, k, p)) % p)