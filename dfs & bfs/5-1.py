# 음료수 얼려 먹기
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if array[x][y] == 0:
        array[x][y] = 1
        # 상, 하, 좌, 우를 재귀적으로 호출하는 방법.
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(list(map(int, input())))

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)
