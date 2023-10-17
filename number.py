#find the largest of two number
num1=int(input('give me a number: '))
num2=int(input('give me a other number: '))
if num1<num2:
    print(num2,'is big')
elif num1==num2:
    print('both are equal')
else:
    print(num1,'is big')
#find the largest of 3 number
n1=int(input('put 1st number: '))
n2=int(input('put 2nd number: '))
n3=int(input('put 3rd number: '))
li=[n1,n2,n3]
largest=max(li)
print(largest)
if n1>n2 and n1>n3 :
    print('n1 is big')
elif n2>n1 and n2>n3:
    print('n2 big')
else:
    print('n3 is big')
# average number
lens = int(input('how many number do want put? : '))
nums=[]
for i in range(0,lens):
    number= int(input('put your numbers: '))
    nums.append(number)
print(round(sum(nums)/lens,3))
numb=[]
while len(numb)<lens:
    no = int(input('give me your number : '))
    numb.append(no)
print(sum(numb)/lens)
#divisible by 3 and 5
def divisible(num):
    result=[]
    for i in range(0,num+1):
        if i%3==0 and i%5==0:
            print(i)
divisible(20)
