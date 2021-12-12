"""
문제의 의도와 다르게 푼 것 같다.
우선 주어진 추로 만들 수 있는 합(weight_sums)을 구한다.
weight_sums를 정렬한다.
주어진 구슬의 무게가 weight_sums에 있으면 True를 반환한다.
없다면 weight_sums를 순서대로 주어진 구슬의 무게와 더하여 해당 값이 weight_sums에 있는지 확인한다.

처음 생각할 때 주어진 구슬의 무게 + weight_sum[i] = weight_sum[j]일 때 i, j에 추가 중복으로
사용될 경우 때문에 헷갈렸는데, 중복으로 사용된 경우에는 해당 추를 사용하지 않는 것과 같아서
아무 문제가 없다.

findSums를 최적화 하는 방법이 있다.
reference: https://www.acmicpc.net/source/21446534
바로 value = sums[idx] + weight이외에도 value_add = abs(sums[idx] - weight)를 추가하는 것이다.
이를 통해 canPossible 함수가 필요 없게 되고 for문을 무의미하게 한번 더 실행할 필요가 없어진다.

* set은 생각보다 빠르다...
"""

def findSums():
    sums = []
    for weight in weights:
        for idx in range(len(sums)):
            value_add = sums[idx] + weight
            value_sub = abs(sums[idx] - weight)
            
            sums.append(value_add)
            sums.append(value_sub)

        sums.append(weight)
    
    return list(set(sums))

num_weight = int(input())
weights = list(map(int, input().split()))

num_stuff = int(input())
stuffs = list(map(int, input().split()))

weight_sums = findSums()

for stuff in stuffs:
    print("Y" if stuff in weight_sums else "N", end=' ')