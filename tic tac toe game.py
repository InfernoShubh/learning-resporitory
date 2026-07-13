
player1=input( "name the player (X)")
player2=input( "name the player (O)")
a=b=c=d=e=f=g=h=i=" "

player = "X"

for turn in range(9):
    print(a,"|",b,"|",c)
    print("--+---+--")
    print(d,"|",e,"|",f)
    print("--+---+--")
    print(g,"|",h,"|",i)
    name=player1 if player=="X" else player2
    move = input(f"{name} ({player}), choose position (1-9): ")

    if move=="1" and a==" ": a=player
    elif move=="2" and b==" ": b=player
    elif move=="3" and c==" ": c=player
    elif move=="4" and d==" ": d=player
    elif move=="5" and e==" ": e=player
    elif move=="6" and f==" ": f=player
    elif move=="7" and g==" ": g=player
    elif move=="8" and h==" ": h=player
    elif move=="9" and i==" ": i=player
    else:
        print("Invalid or taken!")
        continue

    if ((a==b==c==player) or (d==e==f==player) or (g==h==i==player) or
        (a==d==g==player) or (b==e==h==player) or (c==f==i==player) or
        (a==e==i==player) or (c==e==g==player)):
        
        if player=="X":
         print(player1,"Wonderful you won this match")
        else:
         print(player2,"Wonderful you won this match")
        
        break

       

    player = "O" if player == "X" else "X"
else:
    print("It's a draw!")

print("Game Over!")
