"""
이전에는 배열들의 합을 dfs로 구현했지만, collecitons의 Counter를 쓰면 더 빠르다.
reference: https://www.acmicpc.net/source/14589108
"""
#!/usr/bin/python
import sys
from collections import Counter

input = sys.stdin.readline

def findSubSum(sub_sum, sub_arr):
    for element in sub_arr:
        tmp_sum = [element + basis for basis in sub_sum]
        sub_sum += tmp_sum


n, s = map(int, input().split())
arr = list(map(int, input().split()))

border = n // 2
sub_a, sub_b = arr[:border], arr[border:]
sub_a_sum, sub_b_sum = [0], [0]

findSubSum(sub_a_sum, sub_a)
findSubSum(sub_b_sum, sub_b)

b_counter = Counter(sub_b_sum)

count = 0 if s != 0 else -1

for element in sub_a_sum:
    target = s - element
    if target in b_counter:
        count += b_counter[target]

print(count)