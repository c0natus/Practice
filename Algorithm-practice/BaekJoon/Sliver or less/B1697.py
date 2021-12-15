"""
좀더 생각해서 예외 처리를 해서 시간을 줄이자
reference: https://www.acmicpc.net/source/23747535
"""

def find(n, k):
    if n >= k:
        # 뒤로 가는 경우는 -1 이동만 있기 때문이다.
        return n - k
    elif k == 1:
        # n이 0이고 k가 1인 경우 *2의 움직임보단 +1 움직임으로 찾는다.
        return 1
    elif k % 2 == 0:
        # k가 짝수인 경우 k를 n만큼 뒤로 이동한 경우와
        # 2로 나눈 후 찾은 이동 수 중 더 작은 값을 반환한다.
        return min(k-n, find(n, k//2) + 1)
    else:
        # k가 홀수인 경우 앞, 뒤로 1씩 이동한 후
        # 이동 경우의 수 중 작은 값을 반환한다.
        return min(find(n, k-1), find(n, k+1)) + 1

print(find(*map(int, input().split())))