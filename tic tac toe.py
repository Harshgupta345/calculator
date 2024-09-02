import random
import numbers
list=[]
vui=[]
op=[]
count=0
print("welcome to Tic Tac Toe")
turn=1
print("enter 1 to play with computer\n enter 2 to play with local")
ui=int(input("enter:"))
def sum(a,b,c):
    return a+b+c
xstate=[0,0,0,0,0,0,0,0,0]
zstate=[0,0,0,0,0,0,0,0,0]

def printboard(xstate,zstate):
    print(f"{'X' if xstate[0] else('O' if zstate[0] else 0)}|{'X' if xstate[1] else('O' if zstate[1] else 1)}|{'X' if xstate[2] else('O' if zstate[2] else 2)}")
    print(f"-----")
    print(f"{'X' if xstate[3] else('O' if zstate[3] else 3)}|{'X' if xstate[4] else('O' if zstate[4] else 4)}|{'X' if xstate[5] else('O' if zstate[5] else 5)}")
    print(f"-----")
    print(f"{'X' if xstate[6] else('O' if zstate[6] else 6)}|{'X' if xstate[7] else('O' if zstate[7] else 7)}|{'X' if xstate[8] else('O' if zstate[8] else 8)}")
    pass
def chkwin(xstate,zstate):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(sum(xstate[win[0]],xstate[win[1]],xstate[win[2]])==3):
            print("game over ",a,"is winner")
            return 1
        if(sum(zstate[win[0]],zstate[win[1]],zstate[win[2]])==3):
            print("game over ",b,"is winner")
            return 0
        else:
          return -1
if(ui==2):
    a=input("enter X player name")
    b=input("enter O player name")
    while (True):
        if (turn==1):
            print(a,"'s chances")
            value=int(input("plz enter a value:"))
            xstate[value]=1
            printboard(xstate,zstate)
        else:
            print(b,"'s chances")
            value=int(input("plz enter a value:"))
            zstate[value]=1 
            printboard(xstate,zstate)
        chj=chkwin(xstate,zstate)
        if(chj!= -1):
            break
        turn=1-turn   
elif (ui==1):
    a=input("enter  player name")
    b=random.randint(1,2)
    if (b==1):
        while(count<10):
          count=count+1
          if (turn==1):
            print(a,"'s chances")
            value=int(input("plz enter a value:"))
            list.append(value)
            xstate[value]=1
            printboard(xstate,zstate)

          else:
            print("computer's chances")
            value=random.randint(0,8)
            zstate[value]=1
            printboard(xstate,zstate)
          turn=1-turn
        chj=chkwin(xstate,zstate)
        if(chj==1):
            print(a,"is winner")
        if (chj==0):
            print("comp is winner")
            
        
    if (b==2):
        while (count<10):
          count=count+1
          if (turn==1):
            print("computer's chances")
            value=random.randint(0,8)
            xstate[value]=1
            printboard(xstate,zstate)
            
          else:
            print(a,"'s chances")
            value=int(input("plz enter a value:"))
            zstate[value]=1
            printboard(xstate,zstate)
          turn=1-turn
        chj=chkwin(xstate,zstate)
        if(chj==1):
            print("comp is winner")

        if(chj==0):
            print(a,"is winner")
            
    
    
print("match over")



   