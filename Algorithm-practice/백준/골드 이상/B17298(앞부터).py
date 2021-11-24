import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
ans = [-1]*len(arr)
stack = []
size = 0
for i in range(len(arr)):
    #  스택의 사이즈를 판단한다.
    while size != 0:
        # 스택의 사이즈가 0이 아닐 때, i 번째 arr의 값이
        # 스택의 제일 윗부분과의 대소관계를 판단한다.
        if stack[-1][1] < arr[i]:
            # 스택의 제일 윗 부분보다 큰 수가 나왔을 때,
            # 이것을 만족할 때까지 pop을 하고 그 값을 ans
            # 배열에 저장한다.
            idx, val = stack.pop()
            ans[idx] = arr[i]
            size -= 1
        else:
            # 스택의 제일 윗 부분보다 작은 수일 때,
            # 계속해서 스택에 push한다.
            stack.append([i, arr[i]])
            size += 1
            break
    
    if size == 0:
        # 스택의 사이즈가 0일 때, i 번째 arr의 값을 넣어준다.
        stack.append([i, arr[i]])
        size += 1
    
print(' '.join(list(map(str, ans))))