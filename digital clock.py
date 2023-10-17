from datetime import datetime
import time
hour= int(input('Type in the current hour: '))
minute=int(input('Type in the current minute: '))
sec=int(input('Type in the current sec: '))
def display():
    print(hour,':',minute, ': ',sec,': ')
def add():
    global hour
    global minute
    global sec

    sec=sec+1
    if sec==60:
        minute=minute+1
        sec=0
    if minute==60:
        hour=hour+1
        minute=0
    if hour==24:
        hour=0
print('/n')
while True:
    time.sleep(1)
    add()
    print(display())
