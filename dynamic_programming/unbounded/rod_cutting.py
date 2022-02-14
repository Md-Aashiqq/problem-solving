
# problem cutting the rod into subrod order to max profit
# given 
#  lenght = [1,2,3,4]
#  price = [1,5,8,9]
# len = 4
# cutting the rod into 2 | 2 => 5 + 5 = 10 

def solve(lenght,price,max_lenght,n,memo):

    if n==0 or max_lenght == 0:
        return 0
    
    if lenght[n-1] > max_lenght:
        memo[n][max_lenght] = solve(lenght,price,max_lenght,n-1,memo)
    
    else:
        memo[n][max_lenght] = max(solve(lenght,price,max_lenght,n-1,memo),price[n-1]+solve(lenght,price,max_lenght-lenght[n-1],n,memo))

    return memo[n][max_lenght]


length = [1,2,3,4,5,6,7,8]
price= [1, 5, 8, 9, 10, 17, 17, 20]

memo = [ [0 for _ in range(len(length)+1)] for _ in range(len(length)+1)]

print(solve(length,price,len(length),len(price),memo))