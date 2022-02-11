
#  A = [1 6 11 5]

# 1st way = [1,6] [11, 5] = ads(7-16) = 9
#  ans 2nd wat [1,6,5] [11] = abs(12-11) = 1

# A 

def minimumDifference(nums):
    
        
    totalSum = sum(nums)
    n = len(nums)
    dp = [[False for _ in range(totalSum+1)] for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = True
    for i in range(1,totalSum+1):
        dp[0][i] = False

    for i in range(1,n+1):
        for j in range(1,totalSum+1):
            
            if nums[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
    print(dp)
    diff = float("Inf")

    for i in range(totalSum//2,-1,-1):
        first = i
        second = totalSum -i
        if dp[n][i] == True:
            cal = abs(first - second)
            diff = min(diff,cal)
    
    return diff

arr = [-36,36]

print(minimumDifference(arr))