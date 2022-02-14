
# arr = [1,2,5]
# target = 6
# ans possiblites = 4

def solve(arr,target,n):

    dp = [[0 for _ in range(target+1)] for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = 1
    
    for i in range(target+1):
        dp[0][i] = 0

    print(dp)

    for i in range(1,n+1):
        for j in range(1,target+1):

            if arr[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-arr[i-1]]
    return dp[n][target]

arr = [2, 5, 3, 6]
target = 10
print(solve(arr,target,len(arr)))