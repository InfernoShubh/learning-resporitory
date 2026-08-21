n=int(input("value:"))
for i in range(n,0,-1):
    for j in range(0,n+1):
        if i==n or j==i-1 or j==0:
            print("*",end="")
        else:
            print(" ",end="")
    print()