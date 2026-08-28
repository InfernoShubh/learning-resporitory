import random as rd
a=rd.randint(0,100)
for i in range(0,5):
    num=int(input("Guess a num between 0 to 100:"))
    if a==num:
        print("wow! you guessed it")
        break
    elif a>=num:
        print("Go Higher")      
    elif num>=a:
        print("Go Lower ")
else:
       print("oh! better lucknext time")

