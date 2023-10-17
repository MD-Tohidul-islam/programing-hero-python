num=123
rev2=0
while num>0:
    last=num%10
    rev2=rev2*10+last
    num=num//10
print(rev2)
