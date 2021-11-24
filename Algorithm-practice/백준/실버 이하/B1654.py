#!/usr/bin/python

def countSplit(criterion):
    ret = 0
    for i in lan:
        ret += i // criterion
    return ret

def findLength(target_count, left, right):
    answer = 0
    while left <= right:
        mid = (left+right) // 2
        if target_count <= countSplit(mid):
            # 기준과 같거나 더 많을 때
            answer = mid
            left = mid + 1
        else:
            # 기준 보다 더 적을 때
            right = mid - 1

    return answer


k, n = map(int, input().split())
lan = sorted([int(input()) for _ in range(k)])
answer = findLength(n, 1, lan[-1])
print(answer)