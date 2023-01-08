# 게임 개발
def turnLeft():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


n, m = map(int, input().split())
# 방문할 위치를 저장하기 위한 맵 필요
d = [[0]*m for _ in range(n)]

x, y, direction = map(int, input().split())
# 현재 좌표 방문 처리
d[x][y] = 1
gameMap = list()
# 맵 만들기
for i in range(n):
    gameMap.append(list(map(int, input().split())))

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 1
turn_time = 0

while True:
    turnLeft()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and gameMap[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        # 뒤로 갈 수 있다면 이동 해야함
        nx = x - dx[direction]
        ny = y - dy[direction]
        if gameMap[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
# 이 문제는 지정된 맵을 바꾸면서 나아가는 것이 아닌, 방문한 칸을 표시하는 별도의 배열을 요구함.
# 그렇게 하지 않고 0 -> 1 로 바꾸며 나가면 바다로 인식한다.
# 바다와 방문한 칸의 기능이 조금은 달라 새로운 배열 공간이 필요하게 된 것.
