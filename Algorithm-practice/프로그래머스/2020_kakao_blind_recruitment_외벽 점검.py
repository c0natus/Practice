# 단순 순열만 가지고는 시간 초과가 나왔다.
# 원순열을 적용해서 통과하였다.
# 하지만 다른 풀이를 보니 훨씬 간단하게 하였다.....

from itertools import permutations
from collections import deque
import copy


def removeWeak(n, person, weak, start):

    end = start + person    
    i = 0
    size = len(weak)

    if end >= n:
        end_mod = end % n
        while i < size:
            if 0 <= weak[i] <= end_mod or start <= weak[i] < n:
                nxt_start = weak[(i+1)%size]
                weak.pop(i)
                size -= 1
            else:
                i += 1
    else:
        while i < size:
            if start <= weak[i] <= end:
                nxt_start = weak[(i+1)%size]
                weak.pop(i)
                size -= 1
            else:
                i += 1       
                
    return weak, nxt_start


def canRemoveAll(n, order, weak, start):
    tmp_weak = copy.deepcopy(weak)
    for person in order:
        tmp_weak, nxt_start = removeWeak(n, person, tmp_weak, start)
        start = nxt_start
        if not tmp_weak:
            return True
    
    return False


def isPossible(n, weak, selected_list):

    if len(selected_list) != 1:
        orders = permutations(selected_list[:-1])
        orders = list(map(list, orders))
        for order in orders:
            for start in weak:
                if canRemoveAll(n, order+[selected_list[-1]], weak, start):
                    return True
            if len(selected_list) <= 2:
                break
        return False

    else:
        orders = [[selected_list[0]]]
        for order in orders:
            for start in weak:
                if canRemoveAll(n, order, weak, start):
                    return True
            if len(selected_list) <= 2:
                break
        return False


def solution(n, weak, dist):
    dist.sort()
    selected_list = []
    dist_size = len(dist)
    for i in range(dist_size-1, -1, -1):
        selected_list.append(dist[i])
        if isPossible(n, weak, selected_list):
            break
        if i == 0:
            return -1
    return len(selected_list)


n = [12,12,12]
weak = [
    	[1, 5, 6, 10],
        [1, 3, 4, 9, 10],
        [0, 10],
    ]
dist = [
        [1, 2, 3, 4],
        [3, 5, 7],
        [1, 2]
    ]

for i in range(3):
    print(solution(n[i], weak[i], dist[i]))