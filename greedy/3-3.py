# 모험가 길드
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0  # 현재 그룹에 포함된 모험가의 수

for x in data:
    count += 1  # 하나씩 증가 시켜서,
    if count >= x:  # 현재 포함된 모험가의 수가 현재 공포도 이상이면, result 넣고 그룹 결성
        result += 1
        count = 0
# 정렬까지 생각했지만 이후 그룹을 짓는 것에 대한 생각을 하지 못함.
# count 하나씩 넣어보면서 확인하는 방법

print(result)
