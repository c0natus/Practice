# 처음엔 엄청난 예외처리로 시도했다.
# 당연히 처리 못한 예외들이 많았다.
# 풀이를 찾아보고 훨씬 간단한 방법이 있다는 것을 알게 되었다.

def isPossible(answer):
    for col, row, val in answer:
        if val == 0:
            # 기둥
            if row == 0 or (col, row-1, 0) in answer or (col-1,row,1) in answer or (col,row,1) in answer:
                # 바닥일 경우, 밑에 기둥일 경우, 보가 있는 2가지 경우
                continue
            else:
                return False
        else:
            #보
            if (col, row-1, 0) in answer or (col+1, row-1, 0) in answer or ((col-1,row, 1) in answer and (col+1, row, 1) in answer):
                # 밑에 기둥일 경우, 오른쪽 끝 밑이 기둥일 경우, 좌우에 보가 있는 경우
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = set()

    for col, row, val, build in build_frame:
        stuff = (col, row, val)

        if build == 0:
            # 삭제
            answer.remove(stuff)
            if not isPossible(answer):
                answer.add(stuff)
        else:
            answer.add(stuff)
            # 추가
            if not isPossible(answer):
                answer.remove(stuff)

    answer = list(map(list, answer))
    return sorted(list(answer))

n = [5,5]
# x, y, 기둥/보, 삭제/설치
build_frame = [
    	[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]],
        [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]],    
    ]

for i in range(2):
    print(solution(n[i], build_frame[i]))