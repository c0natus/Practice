from itertools import combinations

def make_case(info):
    ret = {}
    for i in info:
        arr = i.split()
        arr, score = arr[:4], arr[4]
        for r in range(5):
            combi = combinations(arr, r)
            for c in combi:
                if c in ret:
                    ret[c].append(int(score))
                else:
                    ret[c] = [int(score)]
    
    for tmp_key in ret.keys():
        ret[tmp_key].sort()

    return ret


def parse_key(arr):
    key_tuple = []
    for i in arr[:4]:
        if i == '-':
            continue
        else:
            key_tuple.append(i)
    return tuple(key_tuple)


def search(arr, score, size):
    if size == 0 or (size >= 1 and score > arr[-1]):
        return size
    
    start, end = 0, size-1
    while(start < end):
        mid = (start+end) // 2
        if arr[mid] < score:
            start = mid + 1
        else:
            end = mid
    
    return end



def solution(info, query):
    info_all_case = make_case(info)
    answer = []
    for q in query:
        q_arr = q.replace(' and ', ' ').split()
        key_tuple = parse_key(q_arr)
        score = int(q_arr[4])
        if key_tuple in info_all_case:
            size = len(info_all_case[key_tuple])
            target = search(info_all_case[key_tuple], score, size)
            answer.append(size - target)
        else:
            answer.append(0)

    return answer

print(solution(
    ["java backend junior pizza 150"],
    ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
))