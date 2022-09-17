li = [[1,2,3,4],
      [5,6,7,8],
      [9,10,11,12],
      [13,14,15,16]]

m = len(li)
n = len(li[0])

k = 0
l = 0
  
''' k - starting row index
        m - ending row index
        l - starting column index
        n - ending column index
        i - iterator '''
  
while (k < m and l < n):
  
        # Print the first row from
        # the remaining rows
    for i in range(l, n):
        print(li[k][i], end=" ")
  
    k += 1
  
        # Print the last column from
        # the remaining columns
    for i in range(k, m):
        print(li[i][n - 1], end=" ")
  
    n -= 1
  
        # Print the last row from
        # the remaining rows
    if (k < m):
  
        for i in range(n - 1, (l - 1), -1):
            print(li[m - 1][i], end=" ")
  
        m -= 1
  
        # Print the first column from
        # the remaining columns
    if (l < n):
        for i in range(m - 1, k - 1, -1):
            print(li[i][l], end=" ")
  
        l += 1
'''print()
top = 0
bottom = len(li)
left = 0
right = len(li[0])

while top < bottom and left < right:
    for i in range(left,right):
        print(li[top][i], end=" ")
    top += 1
    
    for i in range(top,bottom):
        print(li[i][right-1], end=" ")
    right -= 1
    if top < bottom :
        for i in range(right-1,left-1,-1):
            print(li[bottom-1][i], end=" ")
        bottom -= 1
    if right < left :
        for i in range(bottom-1,top-1,-1):
            print(li[i][left], end=" ")
        left += 1
        '''