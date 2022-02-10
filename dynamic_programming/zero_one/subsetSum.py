
#  arr = [1,2,3]
#  sum = 5

from asyncio import FastChildWatcher


def subsetSum_with_dp(arr,sum1,n):

    dp = [[False for _ in range(sum1+1)] for _ in range(n+1)]

    # If sum is 0, then answer is true
    for i in range(n + 1):
        dp[i][0] = True
         
    # If sum is not 0 and set is empty,
    # then answer is false
    for i in range(1, sum1 + 1):
         dp[0][i]= False
    
    print(dp)
    for i in range(1,n+1):
        for j in range(1,sum1+1):
            if j < arr[i-1]:
                dp[i][j] = dp[i-1][j]
            if  j >= arr[i-1]:
                dp[i][j] = (dp[i-1][j] or dp[i-1][j-arr[i-1]])
    print(dp)
    return dp[n][sum1]


    

def subsetSum_with_resurrsion(arr,sum1,n):
    
    if sum1 == 0:
        return True
    
    if sum1 != 0 and n == 0 :
        return False
    
    if arr[n-1] > sum1:
        subsetSum_with_resurrsion(arr,sum1,n-1)
    else:
        return subsetSum_with_resurrsion(arr,sum1,n-1) or subsetSum_with_resurrsion(arr,sum1-arr[n-1],n-1)
    

arr = [1,2,3]
su = 5

print(subsetSum_with_dp(arr,su,len(arr)))