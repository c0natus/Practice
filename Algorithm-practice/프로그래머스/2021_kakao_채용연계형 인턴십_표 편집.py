class Node:
    def __init__(self, i, prev, nxt):
        self.id = i
        self.p = prev
        self.n = nxt
        
def init_nodes(n):
    nodes = [None] * n
    nodes[0] = Node(0,None, None)
    for i in range(1, n):
        nodes[i] = Node(i, nodes[i-1], None)
        
    for i in range(n-1):
        nodes[i].n = nodes[i+1]
        
    return nodes
    
def solution(n, k, cmd):
    removed_stack = []
    nodes = init_nodes(n)
    first = nodes[0]
    select = nodes[k]
    for c in cmd:
        if c[0] == 'U':
            for _ in range(int(c[2:])):
                select = select.p
        elif c[0] == 'D':
            for _ in range(int(c[2:])):
                select = select.n
        elif c[0] == 'C':
            removed_stack.append(select)
            if select.p is None:
                first = select.n
                first.p = None
                select = first
            else:
                if select.n is None:
                    select.p.n = None
                    select = select.p
                else:
                    select.p.n = select.n
                    select.n.p = select.p
                    select = select.n  
        elif c[0] == 'Z':
            recover = removed_stack.pop()
            if recover.p is None:
                first = recover
                recover.n.p = recover
            else:
                if recover.n is None:
                    recover.p.n = recover
                else:
                    recover.p.n = recover
                    recover.n.p = recover
    
    answer = ['X'] * n
    node = first
    while node is not None:
        answer[node.id] = 'O'
        node = node.n
    return ''.join(answer)

print(solution(8, 0, ["C","C","C","C","C","Z","Z","Z"]))