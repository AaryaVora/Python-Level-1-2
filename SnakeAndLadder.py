# recursion
from random import randint 
player1 = 0
player2 = 0
dice = 0
turn = 1
ladderHead = [1,4,8,21,28,50,71,80]
ladderTail = [38,14,30,42,76,67,92,99]
snakeHead = [32,36,48,63,88,95,97]
snakeTail = [10,6,26,18,24,56,78]

def check(pos):
    if pos in ladderHead :
        print("++++++++++Found a ladder!+++++++++++++")
        return ladderTail[ladderHead.index(pos)]
    elif pos in snakeHead:
        print("-------You were bitten by the snake!-----------")
        return snakeTail[snakeHead.index(pos)]
    return pos
      
def rollDice ():
    x = randint(1,6)
    if x == 6:
        x+=rollDice()
    return x
    


while True :
    if player1 >= 100 or player2 >= 100:
        break 

    dice = rollDice()
    if dice > 17:
        dice = 0
    if turn % 2 != 0:
        print("Player1's turn current position =",player1,"Dice value =",dice)
        if player1 + dice <= 100 :

            player1 += dice
            player1 = check(player1)
    
    else: 
        print("Player2's turn current position =",player2,"Dice value =",dice)
        if player2 + dice < 100 :
            player2 += dice
            player2 = check(player2)
    
    # print ("Player 1",player1,"dice", dice,"Player 2",player2 )
    turn += 1