p= int(input("give me a number: "))
prime=[]
for e in range(2,p+1):
    for o in range(2,e):
        if e%o==0:
            break
    else:
        prime.append(e)
print(prime)

def is_prime(v):
    for i in range(2,v):
        if v%i==0:
            return False
    return True
def all_prime(v):
    prime_number = []
    for j in range(2,v+1):
        if is_prime(j) is True:
            prime_number.append(j)
    return prime_number
v=int(input("give me number: "))
prime_number =all_prime(v)

print(prime_number)
n=20
prime=[i for i in range(2,n) if 0 not in[ i%j for j in range(2,i)]]
print(prime)


