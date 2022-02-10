

def solve_with_dp(arr,sumAns,n):

    dp = [[0 for _ in range(sumAns+1)] for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = 1
    for i in range(1,sumAns+1):
        dp[0][i] = 0

    print(dp)

    for i in range(1,n+1):
        for j in range(1,sumAns+1):
            if arr[i-1] > j :
                dp[i][j] = dp[i-1][j]
            elif arr[i-1] <= j:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]]
    print(dp)
    return dp[n][sumAns]
# [1, 1, 0, 0],
# [1, 2, 1, 0], 
# [1, 2, 2, 2], 
# [1, 3, 4, 4]

def solve(arr,sumAns,n):
    if n == 0 and sumAns != 0 :
        return 0
    
    if sumAns == 0:
        return 1

    if arr[n-1] > sumAns:
        return solve(arr,sumAns,n-1)
    else:
        return solve(arr,sumAns,n-1) + solve(arr,sumAns-arr[n-1],n-1)

arr = [1,2,1] 
sumAns = 3

print(solve_with_dp(arr,sumAns,len(arr)))