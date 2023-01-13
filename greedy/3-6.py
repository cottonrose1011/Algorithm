# 볼링공 고르기
n, m = map(int, input().split())
ball = list(map(int, input().split()))

weights = [0] * (m+1)

for data in ball:
    weights[data] += 1

result = 0

for i in range(1, m):
    n -= weights[i]
    result += weights[i] * n
# 특정 볼링공 무게의 개수를 기록 (합은 n개)
# i번째 무게의 볼링공 개수 * i번째 무게보다 높은 무게의 볼링공 개수
print(result)
