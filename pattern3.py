for i in range(0,5):
    for j in range(0,5):
        if i==0 or i==5-1 or j==0 or j==4:
            print("*",end=" ")
        elif j==1:
            print("2",end=" ")
        elif j==2:
            print('3',end=" ")
        elif j==3:
            print("4",end=" ")
        else:
            print("  ",end="")
    print()
