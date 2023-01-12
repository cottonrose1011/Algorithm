# 1로 만들기
x = int(input())
d = [0] * 30001
# ai = min(a(i-1),a(i/2),a(i/3),a(i/5)) + 1 -> 각 솔루션 중 최저로 걸린 거 선택
# 일단 1을 먼저 뺀 값을 저장하고 각각 2, 3, 5로 나누어 떨어질 때의 최소값으로 거른다
# bottom-up 방식
for i in range(2, x+1):
    # +1 은 횟수
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)

print(d)
