# 문자열 재정렬
s = list(input())
s.sort()
sumInt = 0
result = ""

for data in range(len(s)):
    try:
        sumInt += int(s[data])

    except:
        index = data
        break
# isalpha()를 사용해 알파벳 구분 가능.

for i in range(index, len(s)):
    result += s[i]

if sumInt != 0:
    result += str(sumInt)

print(result)
