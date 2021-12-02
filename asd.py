for i in range(8, 19, 4):
    for j in range(1,4):
        if (i % j) >= (j/3):
            if (i/4) <= (j+1):
                print("homer", i, j)
            else:
                print("marge", i, j)
            
        else:
            print("Bart", i, j)