#!/usr/bin/python

# low�� 1, high�� n^2�� �ξ� mid���� ���� ���� ������ ����
# ���� ���� ������ ���ϴ� ���� �ٽ��̴�.

n = int(input())
k = int(input())

low = 1
high = n ** 2

while low < high:
    mid = (low + high) // 2

    count = 0

    for i in range(1, n+1):
        count += min(mid // i, n)
    
    if k <= count:
        high = mid
    else:
        low = mid + 1

print(low)