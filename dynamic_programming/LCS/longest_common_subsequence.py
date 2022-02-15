# find the longest common subsequence
# str1 = "ABCDGH" , str2 = "AEDFHR"
# ans = 3
def solve_by_rescursion(str1,str2,x,y):

    if x == 0 or y == 0:
        return 0
    
    elif str1[x-1] == str2[y-1]:
        return 1 + solve_by_rescursion(str1,str2,x-1,y-1)
    else:
        return max(solve_by_rescursion(str1,str2,x-1,y),solve_by_rescursion(str1,str2,x,y-1))

def solve_by_dp(str1,str2,n,m):

    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,m+1):

            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[n][m]          



str1 = "ABCDGH"
str2 = "AEDFHR"

print(solve_by_rescursion(str1,str2,len(str1),len(str2)))
print(solve_by_dp(str1,str2,len(str1),len(str2)))