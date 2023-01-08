# 시각
n = int(input())
h = 0
m = 0
s = 0
count = 0

while h <= n:
    if h % 10 == 3:
        count += 1
    elif m // 10 == 3 or m % 10 == 3:
        count += 1
    elif s // 10 == 3 or s % 10 == 3:
        count += 1

    s += 1
    if s == 60:
        s = 0
        m += 1
    if m == 60:
        m = 0
        h += 1
    # 이런 식으로 말고 3중 반복문 사용 하면 시, 분, 초를 표현 가능.
    # m == 30, str(m) in '3' -> False, '3' in str(m) -> True.

if h % 10 == 3:
    count -= 1
print(count)
