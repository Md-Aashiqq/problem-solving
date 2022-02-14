#  problem 
#  arr = [1,2,5] min number of coin 
# to form a target => 6
#  note : each coin has included inf times

def solve_by_table(arr,target,n):

    dp = [[0 for _ in range(target+1)] for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = 1
    for j in range(target+1):
        dp[0][j]  = 1e5
    
    for i in range(1,n+1):
        for j in range(1,target+1):

            if arr[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = 1 + min(dp[i-1][j] , dp[i][j-arr[i-1]])
    print(dp)
    return dp[n][target] if dp[n][target] < 1e4 else -1

arr = [2,4]
target =5
n = len(arr)

print(solve_by_table(arr,target,n))
