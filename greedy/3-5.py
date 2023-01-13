# 만들 수 없는 금액
# 동전을 추가해가며 금액을 찾는다, 만들 수 있는 범위를 지정하는 것임.
n = int(input())
coin = list(map(int, input().split()))
coin.sort()

target = 1
for data in coin:
    if data > target:
        break
    else:
        target += data

print(target)
