import string
from random import *

UPPER_ALPHABETS = string.ascii_uppercase
lower_alphabets = string.ascii_lowercase
numbers = string.digits

passlist = [] 
passlist.extend(UPPER_ALPHABETS)              
passlist.extend(lower_alphabets)
passlist.extend(numbers)

shuffle(passlist)

def create_password(length):
    global passlist
    password = ''.join(passlist[0:length])
    return password

if __name__ == "__main__":
  passlen = int(input("Length of your password: "))
  password = create_password(length=passlen)
  print(password)
