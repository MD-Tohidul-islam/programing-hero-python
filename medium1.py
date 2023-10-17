#check armstrong number
n=(input('give me a number to check: '))
sum=0
for i in range(len(n)):
    sum=sum+int(n[i])**len(n)
if sum==int(n):
    print(n,'is an armstrong number')
else:
    print(n,'is not an armstrong number ')
#the solution below from programing hero
def check_armstrong(num):
    order = len(str(num))
    sum=0
    #use temp to find digit.then power it
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**order
        temp//=10
    return num==sum
num=int(input('enter you number: '))
if check_armstrong(num):
    print(num,'is an amstrong number')
else:
    print(num,'is not an amstrong number')
#gcd
def GCD(x,y):
    smaller=min(x,y)
    gcd=1
    for i in range(1,smaller+1):
        if (x%i==0) and (y%i==0):
            gcd=i
    return gcd
num1=int(input('put 1st number: '))
num2=int(input('put 2nd number:'))
gcd=GCD(num1,num2)
print(gcd)
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a=int(input('put a number: '))
b=int(input('put other number: '))
gcd1=gcd(a,b)
print(gcd1)