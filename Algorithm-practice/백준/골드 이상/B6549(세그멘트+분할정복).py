import sys
sys.setrecursionlimit(10**6)


def init_tree(node, start, end):
    if start == end:
        tree[node] = start
        return tree[node]
    else:
        mid = (start+end) // 2
        left = init_tree(node*2, start, mid)
        right = init_tree(node*2+1, mid + 1, end)
        if histo[left] <= histo[right]:
            tree[node] = left
            return tree[node]
        else:
            tree[node] = right
            return tree[node]


def query(node, start, end, left, right):

    if end < left or start > right:
        return None

    if left <= start and end <= right:
        return tree[node]

    mid = (start+end) // 2
    left_index = query(node*2, start, mid, left, right)
    right_index = query(node*2+1, mid+1, end, left, right)

    if left_index is None:
        return right_index
    elif right_index is None:
        return left_index
    else:
        if histo[left_index] <= histo[right_index]:
            return left_index
        else:
            return right_index


def cal_square(left, right):
    global ans
    if left > right:
        return

    # left ~ right 구간 중 제일 작은 높이의 직사각형의 index를 구한다.
    # 그리고 해당하는 높이와 left~right로 넓이 ans와 비교하여 더 큰 값을 저장한다.
    index = query(1, 1, n, left, right)
    ans = max(ans, histo[index] * (right - left + 1))

    # 구한 index를 제외한 나머지 구간 left ~ index - 1, index + 1 ~ right을
    # 위의 과정을 수행하게 한다.
    cal_square(left, index - 1)
    cal_square(index + 1, right)


while True:
    h = input()
    if h == '0':
        break

    h = list(map(int, h.split()))
    n = int(h[0])
    histo = [None] + h[1:]

    # 편의상 세그먼트 트리의 0 인덱스는 사용하지 않는다.
    leaf = 1
    while leaf < n:
        leaf *= 2
    tree = [None] * (2*leaf)
    init_tree(1, 1, n)

    # 분할 정복을 이용해 최대 넓이를 구한다.
    ans = 0
    cal_square(1, n)
    print(ans)