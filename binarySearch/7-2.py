# 정렬된 배열에서 특정 수의 개수 구하기
import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n, x = map(int, input().split())
array = list(map(int, input().split()))

result = 0

if x in array:
    result = bisect_right(array, x) - bisect_left(array, x)
else:
    result = -1

print(result)
