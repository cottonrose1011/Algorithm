# 금광
for tc in range(int(input())):

    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    dp = []
    index = 0
    # 슬라이싱을 활용해 배열 복사 하는 방법
    for i in range(n):
        dp.append(array[index: index + m])
        index += m
    for j in range(1, m):
        for i in range(n):
            if i == 0:
                # 0 위에는 없다!
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            if i == n-1:
                # n-1 밑에는 없다!
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            left = dp[i][j-1]
            # 최대값으로 최신화 하면서 반복
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)
    print(dp)
