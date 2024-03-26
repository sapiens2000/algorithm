# 지정한 방향 일직선
# 벽 or 이미 방문 or 장애물 -> 다음 방향
# 방향 없으면? 처음 방향 부터 다시
# 이동 불가능 하면 멈춤

r, c = map(int, input().split())
k = int(input())
robot_x = 0
robot_y = 0

# -1 : 미방문, -2 : 장애물
maps = [[-1 for _ in range(c)] for _ in range(r)]
for _ in range(k):
    x, y = map(int, input().split())
    maps[x][y] = -2

robot_x, robot_y = map(int, input().split())
maps[robot_x][robot_y] = 0
heads = list(map(int, input().split()))

# 상하좌우
directions = {
    1: [-1, 0],
    2: [1, 0],
    3: [0, -1],
    4: [0, 1]
}

# 위치 저장 변수
head = 0
turn_time = 0

while True:
    if turn_time > 4:
        break
    # 이동 가능한지 검사
    nx = robot_x + directions[heads[head]][0]
    ny = robot_y + directions[heads[head]][1]
    # 벽 아니고
    if 0 <= nx < r and 0 <= ny < c:
        # 방문 X
        if maps[nx][ny] == -1:
            maps[nx][ny] = maps[robot_x][robot_y] + 1
            robot_x, robot_y = nx, ny
            turn_time = 0
        else:
            head = (head + 1) % len(heads)
            turn_time += 1
    else:
        head = (head + 1) % len(heads)
        turn_time += 1


print(robot_x, robot_y)
