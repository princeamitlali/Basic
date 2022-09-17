m = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

def transpose(m):
    for i in range(len(m)):
        for j in range(i+1,len(m[0])):
            m[i][j],m[j][i] = m[j][i],m[i][j]
    return m
        
def rotate(m):
    m = transpose(m)
    return m[::-1]
print(rotate(m))