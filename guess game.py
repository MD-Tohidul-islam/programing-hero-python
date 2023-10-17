import random

print('press q to stop game ')
score=0
while True:
    number=random.randint(0,10)
    guess=input('guess a number between 0 to 10: ')
    if guess=="q":
        print('game over!')
        break
    #guess=int(guess)
    if number==guess:
        print('you got 10 points ')
        score+=10
        print('your new score is:',score)

    else:
        print('your guess did not match')
        print('the number was: ',number)
