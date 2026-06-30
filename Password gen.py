#2nd MINI PROJECT
#RANDOM PASSWORD GENERATOR

import random
import string

password_len=8
charValues=string.ascii_letters+string.punctuation

#List Comprehension [Function for i range ]
#Here we done this one line , and ["".join] means it will join every letters or which elements u stored in our list

password="".join([random.choice(charValues) for i in range(password_len)])

print("Your Random Password is :", password)