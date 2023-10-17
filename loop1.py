#2nd largest number
list1=[22,66,44,33,22,2,5,67,87,97,64]
big1=list1[0]
big2=list1[0]
for i in list1:
    if i>big1:
        big2=big1
        big1=i
print(big2)
list1.sort()
max2=list1[-2]
print(max2)
#2nd smallest number
list2=[55,78,88,99,78,43,49,66,35,77,44]
list2=sorted(list2)
print(list2[1])

#add two list each elements
l1=[1,2,3,4,5,6,5]
l2=[7,8,9,10,11,12,8]
l3=[]
for i in range(0,len(l1)):
    l3.append(l1[i]+l2[i])
print(l3)
l4=[l2[i]-l1[i] for i in range(len(l2))]
print(l4)