# 참고 사이트: https://jason9319.tistory.com/113

import sys
input = sys.stdin.readline

def lowerBound(element):
    left = 0
    right = len(answer) - 1

    while left < right:
        mid = (left + right) // 2

        if answer[mid] < element:
            left = mid + 1
        else:
            right = mid
    
    return left

n = int(input())
A = list(map(int, input().split()))

answer = [A[0]]

for element in A[1:]:
    if answer[-1] < element:
        answer.append(element)
    else:
        substitute_index = lowerBound(element)
        answer[substitute_index] = element

print(len(answer))