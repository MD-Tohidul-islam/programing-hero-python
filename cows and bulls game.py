import random
secret_number=str(random.randint(1000,9999))
print('guess the number in 4 digits')
remaining_try=7
def get_bulls_cows(number,user_guess):
    bulls_cows=[0,0]#cows then bulls
    for i in range(len(number)):
        if user_guess[i]==number[i]:
            bulls_cows[0]+=1
        elif user_guess[i] in number:
            bulls_cows[1]+=1
    return bulls_cows
while remaining_try>0:
    player_guess=input('enter your guess: ')
    if player_guess=='q':
        print('game over!')
        break
    if player_guess==secret_number:
        print('yes. you guessed it!')
        print('you win!')
    else:
        bulls_cows=get_bulls_cows(secret_number,player_guess)
        print('bulls: ',bulls_cows[0])
        print('cows: ',bulls_cows[1])
        remaining_try-=1
        if remaining_try<1:
            print('you lost the game ')
            break