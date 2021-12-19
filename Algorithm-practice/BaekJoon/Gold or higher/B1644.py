#!/usr/bin/python
"""
최적화 1: 에라토스테네스의 체에서 math.sqrt(n) + 1까지만 돌기
최적화 2: 에라토스테네스의 체에서 is_prime을 세팅해주는 방법 바꾸기
"""
import sys
import math
input = sys.stdin.readline

def findPrimes(n):
    is_prime = [False, False] + [True] * (n-1)

    for i in range(2, int(math.sqrt(n))+1):
        if is_prime[i] is True:
            is_prime[i+i::i] = [False] * (n // i - 1)
            # for j in range(i+i, n+1, i):
            #     is_prime[j] = False
        
    return [p for p in range(n+1) if is_prime[p]]

N = int(input())
primes = findPrimes(N)
left = 0
right = 0
count = 0
sum_continuous_prime = 0

for right in range(len(primes)):
    sum_continuous_prime += primes[right]
    if sum_continuous_prime == N:
        count += 1
    while sum_continuous_prime >= N and left <= right:
        sum_continuous_prime -= primes[left]
        left += 1
        if sum_continuous_prime == N:
            count += 1      

print(count)