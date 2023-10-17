def divisible(num):
    result=[]
    for i in range(1,num+1):
        if i%3==0 and i%5==0:
            result.append(i)
    return result
num=int(input('put a number: '))
result=divisible(num)
print(result)
v=int(input('put the number:'))
j=1
while j<v+1:
    if j%3==0 and j%5==0:
        print(j)
    j+=1
#sum of digits
n=int(input('put a number: '))
nums=[]
for i in range(n+1):
    nums.append(i)
print(sum(nums))
nums1=int(input('give a number:' ))
def sum(nums1):
    sum=0
    while nums1>0:
        lastdigit=nums1%10
        sum= sum+lastdigit
        nums1=nums1//10
    return sum
sums=sum(nums1)
print(sums)
n1=input('put a number: ')
sum1=0
for i in n1:
    sum1=sum1+int(i)
print(sum1)
b=str(12345)
c=list(b)
print(c)