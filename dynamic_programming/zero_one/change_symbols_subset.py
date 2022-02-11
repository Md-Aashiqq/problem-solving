#  [1,1,1,1,1]  sum = 3
# ans = 5

# [1,1,1] - [-1,-1] = 3

#  s1 - s2 = diff
#  s1 - sum-s1 = diff
#  2s1 - sum = diff
#  2s1 = sum + diff
#  s1 = sum + diff //2



def solve(arr,cap,n):
    
    dp = [[0 for _ in range(cap+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(1,cap+1):
        dp[0][i] = 0
    
    for i in range(1,n+1):
        for j in range(1,cap+1):

            if arr[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]]
    

    return dp[n][cap]

arr = [1,1,1,1,1]
diff = 3
cap = (diff+sum(arr))//2
print(solve(arr,cap,len(arr)))