import random
import string
def get_password(size):
    all_char=string.punctuation + string.ascii_letters + string.digits+string.whitespace
    password=''
    for char in range(size):
        rand_char=random.choice(all_char)
        password=password+rand_char
    return password
pass_len=int(input('How many charecters in your password?: '))
new_password=get_password(pass_len)
print(new_password)