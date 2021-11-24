def solve(size):
    ans = 0
    for i in range(len(histo)):
        while stack and histo[stack[-1]] > histo[i]:
            width = i
            height = histo[stack[-1]]
            stack.pop()
            if stack:
                width = i - stack[-1] - 1
            ans = max(ans, width * height)
        stack.append(i)

    while stack:
        width = size
        height = histo[stack[-1]]
        stack.pop()
        if stack:
            width = size - stack[-1] - 1
        ans = max(ans, width * height)

    return ans


while True:

    h = input()
    if h == '0':
        break

    h = list(map(int, h.split()))
    n = int(h[0])
    histo = h[1:]
    stack = []

    print(solve(n))
