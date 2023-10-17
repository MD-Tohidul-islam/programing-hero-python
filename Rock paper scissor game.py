
while True:
    p1 = input('1st player input: rock,scissor or paper: ')
    p2 = input('2nd player input: rock,scissor or paper: ')
    if p1=='q' or p2 =='q':
        print('game over!')
        break
    if p1==p2:
        print("it's a tie")
    elif p1=='rock':
        if p2=='scissor':
            print('1st player winner')
        else:
            print('2nd player winner')
    elif p1=='scissor':
        if p2 == 'paper':
            print(' 1st player winner')
        else:
            print('2nd player winner')
    elif p1=='paper':
        if p2 == 'rock':
            print('1st player winner')
        else:
            print('2nd player winner')
    else:
        print('invalid input')

#print(get_winner(player1,player2))