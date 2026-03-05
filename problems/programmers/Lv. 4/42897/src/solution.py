def solution(money):
    case1 = money[:-1]
    case2 = money[1:]

    def dp(arr):
        arr_len = len(arr)
        # Base cases
        if arr_len == 0:
            return 0
        if arr_len == 1:
            return arr[0]
        
        # DP array initialization
        dp = [0] * arr_len
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
        
        # DP calculation
        for i in range(2, arr_len):
            dp[i] = max(dp[i-1], dp[i-2] + arr[i])
        return dp[-1]

    return max(dp(case1), dp(case2))