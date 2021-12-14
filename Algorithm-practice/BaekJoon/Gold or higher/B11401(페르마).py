def fac_mod(n, k, p):
    ret = 1
    for i in range(1, n+1):
        ret = (ret * i) % p
        if i == k:
            fac_dict['k'] = ret
        if i == n-k:
            fac_dict['n-k'] = ret
    fac_dict['n'] = ret



def power_mod(base,expo, p):
    base %= p
    if base == 0:
        return 0
    elif expo == 1:
        return base
    else:
        if expo % 2 == 1:
            return (base * power_mod(base*base, expo//2, p)) % p
        else:
            return power_mod(base*base, expo//2, p)


n,k = map(int, input().split())
p = 1000000007
if n == 1 or n == k or k == 0:
    print(1)
else:
    fac_dict = {'n': 0, 'k': 0, 'n-k': 0}
    fac_mod(n, k, p)
    print((fac_dict['n'] * power_mod((fac_dict['k']*fac_dict['n-k']) % p, p-2, p)) % p)