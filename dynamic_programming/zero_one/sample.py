#  2d array in python

# arr = [[] for _ in range(5)]
arr =  [[0 for _ in range(5)] for _ in range(5)]
print(arr)

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if i==0 or j == 0:
            print(i,j)
            arr[i][j]=1
print(arr)