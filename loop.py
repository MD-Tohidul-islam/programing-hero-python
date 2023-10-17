#sum of squares
n3=int(input('give a number: '))
sq=[]
for j in range(n3+1):
    #sum1=j**2
    sq.append(j**2)
#print(sq)
sum2=sum(sq)
print(sum2)
sum4=0
for i in range(n3+1):
    sum4=sum4+i**2
print(sum4)
sum5=n3*(n3+1)*(2*n3+1)/6
print(sum5)
#sum of elements

n1=[1,2,3,4,5]
s1=sum(n1)
print(s1)
nums=[1,2,3,4,12]
sum=0
for i in nums:
    sum=sum+i
    i+=1
print(sum)
#largest number in list
n2=[4,56,2,9,34,56,76,22,11,6]
big=n2[0]
for i in n2:
    if i>big:
        big=i
print(big,'is largest ')
max1=max(n2)
print(max1)
