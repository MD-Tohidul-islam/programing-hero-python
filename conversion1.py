def decimal_to_binary(n):
    bits=[]
    while n>0:
        bits.append(n%2)
        n=n//2
    bits.reverse()
    binary=''
    for i in bits:
        binary+=str(i)
    return binary

decimal=int(input('give your decimal number: '))
binary=decimal_to_binary(decimal)
print(binary)
#but how can i convert float number into binary
#and aslo binary to decimal