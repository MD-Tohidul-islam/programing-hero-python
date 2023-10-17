#convert miles to kilometers
miles=float(input('distance in miles=: '))
kilometers=miles*1.609344
print('distance in kilometers: ',kilometers)

#celsius to fahrenheit
celsius=float(input('temperature in celsius: '))
fahrenheit=celsius*9/5+32
print('temperature in fahrenheit: ',fahrenheit)
print('temperature conversion program')
print('''press 1 to enter celsius
      press 2 to enter fahrenheit
      press 3 to enter kelvin''')
press = int(input('press your choice: '))
if press<=0 or press>3:
    print('invalid number try again')
elif press==1:
    temp=float(input('enter temperature in celsious:'))
    fahrenheit=round((((9/5)*temp)+32),3)
    kelvin=round((temp+273.15),3)
    print('temperature in fahrenheit: ',fahrenheit,'feg F')
    print('temperature in kelvin: ',kelvin,'deg K')
elif press==2:
    temp = float(input('enter temperature in fehrenheit:'))
    celsius = round((((5 / 9) * temp) - 32), 3)
    kelvin = round(((temp+459.67)*(5/9)), 3)
    print('temperature in celsious: ', celsius, 'feg C')
    print('temperature in kelvin: ', kelvin, 'deg K')
elif press==3:
    temp = float(input('enter temperature in kelvin:'))
    fahrenheit = round(((temp*(9/5))-459.67), 3)
    celsius = round((temp-273.15), 3)
    print('temperature in fahrenheit: ', fahrenheit, 'feg F')
    print('temperature in celsious: ', celsius, 'deg C')
