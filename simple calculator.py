while True:
    def add(n1,n2):
        return n1+n2
    def sub(n1,n2):
        return n1-n2
    def mul(n1,n2):
        return n1*n2
    def div(n1,n2):
        return n1/n2
    def remaider_div(n1,n2):
        return n1%n2
    print('press q to stop operation')
    n1=input('put your 1st number: ')
    if n1 == 'q':
        print('operation is over!')
        break
    operation=input('+ or - or * or / or % :')
    if operation == 'q':
        print('operation is over!')
        break
    n2=input('put your 2bd number: ')
    if n2=='q':
        print('operation is over!')
        break
    n1=int(n1)
    n2=int(n2)
    if operation=='+':
        result=add(n1,n2)
    elif operation=='-':
        result=sub(n1,n2)
    elif operation=='*':
        result=mul(n1,n2)
    elif operation=='/':
        result=div(n1,n2)
    elif operation=='%':
        result=remaider_div(n1,n2)
    else:
        print('invalid input')
    print(result)

