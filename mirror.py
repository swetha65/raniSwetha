def mirror(m):
    for i in range(len(m)//2):
        temp = m[i]
        m[i] = m[len(m)-1-i]
        m[len(m)-1-i] = temp
    return m

m = [[0,1,2], [3,4,5], [6,7,8], [9,10,11]]
print(mirror(m))