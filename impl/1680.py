t = int(input())
for _ in range(t):
    # 가까운 지점부터 방문해 쓰레기를 모은다.
    # 쓰레기장 돌아가는 조건
    # 1. 용량 도달
    # 2. 용량 넘을때 (한번에 실어야함)
    # 3. 지점 다 돌았을때
    # 총 이동거리 구하기.

    w, n = map(int, input().split())
    spots = []
    for _ in range(n):
        spots.append(list(map(int, input().split())))

    result = 0
    weight = 0
    length = 0

    # s[0] : 지점 거리 , s[1] :지점 무게
    for i in range(n):
        length = spots[i][0]

        # 쓰레기 용량이 넘치지 않으면 적재(방문)
        if weight + spots[i][1] < w:
            weight += spots[i][1]
        # 가득 찰 경우 쓰레기장 방문
        elif weight + spots[i][1] == w:
            weight = 0
            result += length
        # 용량이 넘치면 복귀후 실음
        else:
            weight = spots[i][1]
            result += (3*length)

    # 마지막 지점까지 이동 거리
    result += length
    print(result)