# 곱하기 혹은 더하기
s = input()

# 굳이 result = 0 부터 시작할 필요는 없다. result = int(s[0])으로 초기 설정을 하고,
# 반복문의 범위를 (1, len(s))로 돌면 코드의 길이가 줄어듦.
result = 0

for i in range(len(s)):
    # num = int(s[i])
    if i == 0:  # result = int(s[0])으로 할 시 삭제 가능
        result += int(s[i])
    elif s[i] == '0' or s[i] == '1':  # -> num <= 1
        result += int(s[i])
    elif i > 0 and (s[i-1] == '0' or s[i-1] == '1'):  # -> result <= 1 + 위의 조건문과 합치기
        result += int(s[i])
    else:
        result *= int(s[i])

print(result)

