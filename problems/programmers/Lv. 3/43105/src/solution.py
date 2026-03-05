# My solution
def solution(triangle):
    dp = [[] for _ in range(len(triangle))]
    
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            if i == 0:
                dp[i].append(triangle[i][j])    # Basecase
            else:
                if j == 0:  # Left edge
                    dp[i].append(dp[i-1][j] + triangle[i][j])
                elif j == len(triangle[i]) - 1:  # Right edge
                    dp[i].append(dp[i-1][j-1] + triangle[i][j])
                else:  # Middle
                    dp[i].append(max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j])

    return max(dp[len(triangle) - 1])