# 개미 전사
n = int(input())
house = list(map(int, input().split()))
# ai = i번째 식량창고까지의 최적의 해
# [1, 3, 1, 5] -> 1, 3, 3, 8
# ai = max(a(i-1), a(i-2) + k) // i-3 은 고려할 필요가 없음
# 계산된 결과를 저장하기 위해 별도의 DP 테이블 초기화 필수
d = [0] * 100
d[0] = house[0]
d[1] = max(house[0], house[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + house[i])

print(d)
