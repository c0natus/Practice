from itertools import combinations

def solution(orders, course):
    cnt_order_combi = [{} for _ in range(11)]
    for order in orders:
        size = len(order)
        order = sorted(order)
        for i in course:
            if i <= size:
                order_combis = combinations(order, i)
                for combi in order_combis:
                    if combi in cnt_order_combi[i]:
                        cnt_order_combi[i][combi] += 1
                    else:
                        cnt_order_combi[i][combi] = 1
    
    answer = []

    for c in course:
        cnt_max = 0
        course_arr = []
        for name, cnt in cnt_order_combi[c].items():
            if cnt_max < cnt and cnt >= 2:
                course_arr = [name]
                cnt_max = cnt
            elif cnt_max == cnt and cnt >= 2:
                course_arr.append(name)
        for tuple_answer in course_arr:
            answer.append(''.join(tuple_answer))

    return sorted(answer)



o = [["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], ["XYZ", "XWY", "WXA"]]
c = [[2,3,4], [2,3,5], [2,3,4]]

for i in range(3):
    print(solution(o[i], c[i]))