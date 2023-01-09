# 미로 탈출
from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        # 4가지 방향 위치 확인
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if array[nx][ny] == 0:
                continue
            if array[nx][ny] == 1:
                # 맵의 값에 1씩 더해 거리를 측정한다.
                array[nx][ny] = array[x][y] + 1
                queue.append((nx, ny))
    return array[n-1][m-1]
# 헷갈린 부분 : 최소 거리를 한 번에 탐색해 간 것이 아닌 전부 탐색을 하며 거리를 매긴 것임.


n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(list(map(int, input())))

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))
for data in array:
    print(data)
