for i in range(0,100):
    for j in range(0,100):
        for k in range(0,100):
            if i + j + k == 100 and (5*i + 3*j + 0.5*k) == 100:
                print(i,j,k)