# matching given string with pervious string
# index doesnt matter it should be contigous 

# given
# string1 = "ABCDEF" , pattern = "BEF"
# ans= True


def solve(string,pattern,n,m):

    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,m+1):

            if string[i-1] == pattern[j-1]:
          
                dp[i][j] = 1+ dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    print(dp)
    return dp[n][m]


string = "ABCDEF"
pattern = "BEF"

print(solve(string,pattern,len(string),len(pattern)) == len(pattern))