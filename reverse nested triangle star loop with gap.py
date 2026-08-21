row=5
for i in range(row,0,-1):
    for j in range(row-i):
        print(" ",end="")
    for j in range(i):
        if j==0 or j==i-1 or i==row:
          print("*",end="")
        else:
            print(" ",end="")
    print()
