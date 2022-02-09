

def zero_one(weights,values,capacity,n):
    if capacity == 0 or n == 0:
        return 0
    if weights[n-1] > capacity:
        zero_one(weights,values,capacity,n-1)
    
    return max(zero_one(weights,values,capacity,n-1), values[n-1]+zero_one(weights,values,capacity-weights[n-1],n-1))


def zero_one_with_memo(weights,values,capacity,n,memo):

    result = 0;

    if capacity == 0 or n == 0:
        return 0
    if memo[n][capacity] != -1:
        return memo[n][capacity]
    if weights[n-1] > capacity:
        result= zero_one(weights,values,capacity,n-1)
    else:
        result = max(zero_one(weights,values,capacity,n-1), values[n-1]+zero_one(weights,values,capacity-weights[n-1],n-1))
    ans = memo[n][capacity] = result
    return ans


def zero_one_with_table(weights,values,capacity,n):

    dp = [[ -1 for _ in range(capacity+1)] for _ in range(n+1)]
    # print(len(dp[0]))
    for i in range(n+1):
        for j in range(capacity+1):

            if i == 0 or j == 0:
                dp[i][j] = 0
            elif (weights[n-1] > j):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j],values[i-1]+dp[i-1][capacity-weights[i-1]])

    print(dp)
    
    return dp[n][capacity]


val = [1, 2, 3]
wt = [2, 2, 1]
W = 5
n = len(val)

memo = [[-1 for _ in range(W+1)] for _ in range(len(val)+1)]

print(zero_one_with_table(weights=wt,values=val,capacity=W,n=n))
 