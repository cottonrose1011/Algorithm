# 1이 될 때까지
n, k = map(int, input().split())

result = 0

while True:
    # n이 k로 나누어 떨어지는 가장 가까운 수 찾기. 1을 빼는 과정 여러번 한 것과 같음
    target = (n//k) * k
    result += (n - target)
    n = target
    if n < k:
        break
    result += 1
    n //= k

result += (n-1)
print(result)
