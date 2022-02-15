
def findLCS(str1,str2):

    n = len(str1)
    m = len(str2)

    dp = [["" for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,m+1):

            if str1[i-1] == str2[j-1]:
                dp[i][j] =  str1[j-1] + dp[i-1][j-1] 
            else:
                dp[i][j] = dp[i-1][j] if len(dp[i-1][j]) > len(dp[i][j-1]) else dp[i][j-1]
    return dp[n][m]

str1 = "abac"
str2 = "cab"

lcs = findLCS(str1,str2)

p1 =0
p2 = 0

ans = ""

# iterate over the lcs value
for i in lcs:

    # adding char that not match with lcs value to ans string
    
    while(str2[p2] != i):
        ans+=str2[p2]
        p2+=1
    while(str1[p1] != i):
        ans+=str2[p1]
        p1+=1
    ans+=i
    p1+=1
    p2+=1

# adding left charcter in str1 and str2

ans += str1[p1:] + str2[p2:]

print(ans)