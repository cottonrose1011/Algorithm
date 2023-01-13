# 문자열 뒤집기
s = input()

count0 = 0
count1 = 0

if s[0] == '1':
    count1 += 1
else:
    count0 += 1

for i in range(1, len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            count1 += 1
        else:
            count0 += 1

print(min(count0, count1))
