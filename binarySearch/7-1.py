# 떡볶이 떡 만들기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

cake = list(map(int, input().split()))
result = 0
start = 0
end = max(cake)

while start <= end:
    total = 0
    mid = (start + end) // 2
    for data in cake:
        if data > mid:
            total += data - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
# 나는 result 길이를 +- 1씩 하며 계산했지만 이진 탐색으로 길이를 조정하는 것이 더 효율적


print(result)
