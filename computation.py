#simple interest and compound interest
principle=float(input('moneny you borrowed: '))
interest_rate = float(input('interest rate: '))
time_duration=float(input('time duration: '))
compound_interest=principle*(1+interest_rate/100)**(time_duration)
print(compound_interest)
simple_iterest=principle*(interest_rate/100)
print(simple_iterest)

#calculate grades
print('enter your marks')
marks1=int(input('give 1st sub marks: '))
marks2=int(input('give 2nd sub marks: '))
marks3=int(input('give 3rd sub marks: '))
marks4=int(input('give 4th sub marks: '))
marks5=int(input('give 5th sub marks: '))
avg=(marks1+marks2+marks3+marks4+marks5)/5
if avg>100 or avg<0:
    print('invalid')
elif avg>=80:
    print('grade= A+')
elif avg>=70:
    print('grade= A')
elif avg>=60:
    print('grade= A-')
elif avg>=50:
    print('grade= B')
elif avg>=40:
    print('grade = c')
elif avg>=33:
    print('grade= D ')
else:
    print('you are fail')

#gravitational force
import math
#G=6.673*(10**-11)
G=6.673E-11
m1=float(input('put 1st object mass: '))
m2=float(input('put 2nd object mass: '))
r=float(input('enter distance between objects: '))
gravitational_force=(G*(m1*m2))/r**2
print(gravitational_force)