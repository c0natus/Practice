"""
if abs(tmp_sum) < abs(sum_):
을 만족 했을 때도 tmp_sum에 따라 left를 올릴지 right를 내릴지 결정해야 한다.
"""

import sys

input = sys.stdin.readline

input()
arr = list(map(int, input().split()))
arr.sort()

cor = arr[0] + arr[-1]

left = 0
right = len(arr) - 1
sum_ = arr[left] + arr[right]
ans = [arr[left], arr[right]]

while left < right:
    tmp_sum = arr[left] + arr[right]
    if tmp_sum == 0:
        ans = [arr[left], arr[right]]
        break
    if abs(tmp_sum) < abs(sum_):
        sum_ = tmp_sum
        ans = [arr[left], arr[right]]
    
    if tmp_sum < 0:
        left += 1
    else:
        right -= 1

print(ans[0], ans[1])