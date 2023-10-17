v=int(input('give me a number: '))
factors=[]
for i in range(2,v):
    if v%i==0:
        factors.append(i)
print(factors)
m=[]
for j in factors:
    for p in range(2,j):
        if j%p==0:
            break
    else:
        m.append(j)
print(m)
#print(min(m))
o=[5,4,7,9,23,8,56]
min=o[0]
for i in o:
    if i< min:
        min = i
print(min)


