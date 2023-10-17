v=int(input('give me a number and i will tell you is it prime or not:'  ))
for i in range(2,v):
    if v%i==0:
        print('not prime')
        break
else:
    print('prime')
