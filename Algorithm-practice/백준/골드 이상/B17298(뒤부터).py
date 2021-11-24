import sys


def sol():
    N = int(input())
    arr = list(map(int, sys.stdin.readline().split()))
    stack = []
    while N:
        # 끝에서 부터 시작한다.
        N -= 1
        a = arr[N]
        # 스택은 끝에서부터 큰 값들을 유지한다.
        # 스택에 값이 있으나 현재의 값(왼쪽의 값)이 더 크면
        # pop을 수행하고 현재의 값보다 작은 값들을 스택에서 제거한다.
        # 왜냐하면 arr의 왼쪽 값으로 가게되고, 결국 현재 값보다 작은 
        # 오른쪽 값들은 필요가 없기 때문이다.
        while stack and stack[-1] <= a:
            stack.pop()
        # 만약 스택이 비었다며 -1을 출력하고
        # 스택이 있다면 제일 위에 있는 값을 저장한다.
        # 
        arr[N] = str(stack[-1]) if stack else "-1"
        # 그리고 현재 값을 스택에 push한다.
        stack.append(a)
    print(" ".join(arr))


if __name__ == "__main__":
    sol()