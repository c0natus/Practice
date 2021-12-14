from datetime import timedelta

def convertSec(time_format):
    return int(timedelta(
        hours=int(time_format[0:2]),
        minutes=int(time_format[3:5]),
        seconds=int(time_format[6:])
        ).total_seconds())

# 부분 합: 핵심 부분
# 원래는 log_start[i] ~ log_end[i]-1까지 +1을 해주어 합을 구했다.
# 하지만 log_start[i]에 +1, log_end[i]에 -1을 주어 누적합을 구하면 더 빠르다.
# 왜냐하면 처음 방법은 log의 개수에 따라, 구간 길이에 따라 훨씬 느려지기 때문이다.
def initSumArr(play_time, log_start, log_end, size):
    sum_arr = [0] * (play_time+1)
    for i in range(size):
        sum_arr[log_start[i]] += 1
        sum_arr[log_end[i]] -= 1

    for i in range(1, play_time+1):
        sum_arr[i] += sum_arr[i-1]

    return sum_arr

# def initSumArr(play_time, log_start, log_end, size):
#     sum_arr = [0] * (play_time + 1)
#     for i in range(size):
#         for j in range(log_start[i], log_end[i]):
#             sum_arr[j] += 1

#     return sum_arr


def convertFormat(sec):
    m,s = divmod(sec, 60)
    h,m = divmod(m, 60)
    return f'{h:02}:{m:02}:{s:02}'


def solution(play_time, adv_time, logs):
    # 초로 변환하기
    play_time = convertSec(play_time)
    adv_time = convertSec(adv_time)
    size = len(logs)
    logs_start = [None] * size
    logs_end = [None] * size
    for i in range(size):
        logs_start[i] = convertSec(logs[i][:8])
        logs_end[i] = convertSec(logs[i][9:])

    sum_arr = initSumArr(play_time, logs_start, logs_end, size)

    max_sec = sum(sum_arr[:adv_time])
    start_time_sec = 0
    tmp_cnt = max_sec
    for i in range(play_time-adv_time):
        tmp_cnt = tmp_cnt - sum_arr[i] + sum_arr[i+adv_time]
        if max_sec < tmp_cnt:
            max_sec = tmp_cnt
            start_time_sec = i+1

    return convertFormat(start_time_sec)

p = ["02:03:55", "99:59:59", "50:00:00"]
a = ["00:14:15", "25:00:00", "50:00:00"]
l = [
    ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"],
    ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"],
    ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]
]

for i in range(3):
    print(solution(p[i], a[i], l[i]))