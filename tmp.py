import sys

l = sys.stdin.readlines()
n, m, h = map(int, l.pop(0).split())
print(l)
print(*[iter(list(map(int, ll.split())) for ll in l)])
board = list(zip(*[iter(list(map(int, ll.split())) for ll in l)] * m))

print(board)