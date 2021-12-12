"""
문제의 의도와 다르게 푼 것 같다.
우선 주어진 추로 만들 수 있는 합(weight_sums)을 구한다.
weight_sums를 정렬한다.
주어진 구슬의 무게가 weight_sums에 있으면 True를 반환한다.
없다면 weight_sums를 순서대로 주어진 구슬의 무게와 더하여 해당 값이 weight_sums에 있는지 확인한다.

처음 생각할 때 주어진 구슬의 무게 + weight_sum[i] = weight_sum[j]일 때 i, j에 추가 중복으로
사용될 경우 때문에 헷갈렸는데, 중복으로 사용된 경우에는 해당 추를 사용하지 않는 것과 같아서
아무 문제가 없다.
"""

def canPossible(stuff):
    if stuff in weight_sums:
        return True
    
    for one_of_sums in weight_sums:
        if stuff + one_of_sums in weight_sums:
            return True
    
    return False

def findSums():
    sums = []
    for weight in weights:
        previous_sums_len = len(sums)
        for idx in range(previous_sums_len):
            value = sums[idx] + weight
            if value not in sums:
                sums.append(value)
        
        if weight not in sums:
            sums.append(weight)
    
    return sums

num_weight = int(input())
weights = list(map(int, input().split()))

num_stuff = int(input())
stuffs = list(map(int, input().split()))

max_sum = sum(weights)
weight_sums = findSums()

ans = [None] * num_stuff

for idx in range(len(stuffs)):
    if stuffs[idx] <= max_sum:
        if canPossible(stuffs[idx]):
            ans[idx] = 'Y'
            continue
    
    ans[idx] = 'N'

print(' '.join(ans))