#check palindrome
string=input('put your string: ')
string_list=[]
reversed=''
for i in string:
    string_list.append(i)
print(string_list)
string_list.reverse()
for j in string_list:
    reversed+=str(j)
print(string_list)
if string==reversed:
    print('yes,its palindrome')
else:
    print('no, its not palindrome')
rev_str=string[::-1]
if string==rev_str:
    print('string is palindrome ')
else:
    print('string is not palindrome ')
#cube sum
n=int(input('give a number: '))
sum=0
for i in range(0,n+1):
    sum=sum+i**3
print(sum)
sum1=(n*(n+1)/2)**2
print(sum1)