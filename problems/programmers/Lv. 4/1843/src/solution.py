def solution(arr):
    nums = [int(arr[i]) for i in range(0, len(arr), 2)]
    ops  = [arr[i] for i in range(1, len(arr), 2)]
    n = len(nums)

    INF = float('inf')
    dp_max = [[-INF]*n for _ in range(n)]   # n*n max table
    dp_min = [[ INF]*n for _ in range(n)]   # n*n min table

    for i in range(n):
        dp_max[i][i] = dp_min[i][i] = nums[i]

    for length in range(2, n+1):          # 구간 길이
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):         # 분할점
                if ops[k] == '+':
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] + dp_max[k+1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] + dp_min[k+1][j])
                else:  # '-'
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] - dp_min[k+1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] - dp_max[k+1][j])

    return dp_max[0][n-1]