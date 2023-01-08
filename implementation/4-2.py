# 왕실의 나이트
n = input()

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
count = 0

col = 1  # a, b, ..
row = int(n[1])

# 반복문이 아닌 col = int(ord(n[0])) - int(ord('a')) + 1로 표현 하면 코드가 줄어듦
for data in alpha:
    if n[0] == data:
        break
    else:
        col += 1

# 움직일 수 있는 모든 경우의 수
dRow = [1, 1, -1, -1, 2, 2, -2, -2]
dCol = [2, -2, 2, -2, 1, -1, 1, -1]
# 2개의 리스트가 아닌 (1, 2)와 같이 한 개의 리스트도 가능함

for i in range(len(dRow)):
    nRow = row + dRow[i]
    nCol = col + dCol[i]
    if nRow < 1 or nCol < 1 or nRow > 8 or nCol > 8:
        continue
    else:
        count += 1
        print(nCol, nRow)

print(count)
