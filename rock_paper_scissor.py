def rock_paper_scissor(num1,num2,bit1,bit2):
    p1=int(num1[bit1]%3)
    p2=int(num2[bit2]%3)
    if(player_one[p1]==player_two[p2]):
        print("draw")
    elif(player_one[p1]=="rock" and player_two[p2]=="paper"):
        print("player2 wins")
    elif(player_one[p1]=="rock" and player_two[p2]=="rock"):
        print("draw")
    elif(player_one[p1]=="rock" and player_two[p2]=="scissor"):
        print("player1 wins")
    elif(player_one[p1]=="paper" and player_two[p2]=="paper"):
        print("draw")
    elif(player_one[p1]=="paper" and player_two[p2]=="rock"):
        print("player1 wins")
    elif(player_one[p1]=="paper" and player_two[p2]=="scissor"):
        print("player2 wins")
    elif(player_one[p1]=="scissor" and player_two[p2]=="paper"):
        print("player1 wins")
    elif(player_one[p1]=="scissor" and player_two[p2]=="rock"):
        print("player2 wins")
player_one={0:"rock",1:"paper",2:"scissor"}
player_two={0:"paper",1:"rock",2:"scissor"}
while(1):
    num1=input("p1,enter yr choice")
    num2=input("p2,enter yr choice")
    bit1=int(input("enter yr secret number"))
    bit2=int(input("enter yr secret number"))
    rock_paper_scissor(num1,num2,bit1,bit2)
    ch=input("shall u continue r not y/n")
    if(ch=="n"):
        break