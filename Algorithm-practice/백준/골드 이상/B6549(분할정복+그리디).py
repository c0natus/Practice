def merge(start, end, mid, s1, s2):
    ret = max(s1, s2)
    i = j = 0 
    area = histo[mid]
    histo_min = histo[mid]
    while True:
        if mid+i > start:
            if mid+j < end:
                # +1 -1 둘 다 가능할 때
                # 두 방향 중 더 큰 사각형으로 탐색(그리디)
                if histo[mid+i-1] >= histo[mid+j+1]:
                    i -= 1
                    histo_min = min(histo[mid+i], histo_min)
                    area = histo_min * (j - i + 1)
                    ret = max(area, ret)
                else:
                    j += 1
                    histo_min = min(histo[mid+j], histo_min)
                    area = histo_min * (j - i + 1)
                    ret = max(area, ret)    
            else:
                # 오른쪽 끝에 도달했고 왼쪽은 남아있을 때,
                i -= 1
                histo_min = min(histo[mid+i], histo_min)
                area = histo_min * (j - i + 1)
                ret = max(area, ret)
                        
        else:
            if mid+j < end:
                # 왼쪽 끝에 도달했고 오른쪽은 남아있을 때,
                j += 1
                histo_min = min(histo[mid+j], histo_min)
                area = histo_min * (j - i + 1)
                ret = max(area, ret) 
            else:
                # 둘 다 끝에 도달했을 때
                break


    return ret

def cal_square(start, end):
    if start == end:
        return histo[start]
    else:
        mid = (start + end) // 2
        s1 = cal_square(start, mid)
        s2 = cal_square(mid+1, end)
        return merge(start, end, mid, s1, s2)


while True:
    h = input()
    if h == '0':
        break
    
    h = list(map(int, h.split()))
    n = int(h[0])
    histo = h[1:]
    print(cal_square(0, n-1))