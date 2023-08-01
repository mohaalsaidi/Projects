m1 =[[1,2,3],
    [4,5,6]]
m2 =[[1,2,3],
    [4,5,6]]

if len(m1) == len(m2) and len(m1[0]) == len(m2[0]) and len(m1[1]) == len(m2[1]):
    for i in range(len(m1)):
     for j in range(len(m2[0])):
        print( m1[i][j] + m2[i][j])

                       
else:
    print("invalid")
            
