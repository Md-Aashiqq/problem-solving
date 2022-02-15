
memo = {}

def solve(arr,x,l,r,count):

    if x == 0:
        return count
    if x < 0 or l > r:
        return 1e6

    key = str(l)+"*"+str(r)+"*"+str(count)

    if(memo.get(key)):
        return memo.get(key)

    left = solve(arr,x-arr[l],l+1,r,count+1)
    right = solve(arr,x-arr[r],l,r-1,count+1)

    memo[key] = min(left,right)
    return memo[key]
arr = [1,1,4,2,3]
x= 5


print(solve(arr,x,0,len(arr)-1,0)) 
