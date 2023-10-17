m='hello world'
reverse=''
for i in m:
    reverse=i+reverse
print(reverse)
stack=[]
rev=''
for j in m:
    stack.append(j)
for i in range(len(stack),0,-1):
    v=stack.pop()
    rev=rev+v
print(rev)
print(m[::-1])
def recursive(m):
    if len(m)<=0:
        return m
    else:
     return recursive(m[1:])+m[0]
rev1=recursive(m)
print(rev1)
