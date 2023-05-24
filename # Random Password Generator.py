# Random Password Generator
import random
from cryptography.fernet import Fernet

def genRanPassword():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "[]{}()*;/,._-"

    sample = lower + upper + numbers + symbols
    length = 16
    password = "".join(random.sample(sample, length))

    print("Your Password is:", password)




# Random Email Generator
# import random

lower = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
domain = "@gmail.com"

def genRanEmail():
    sample = lower + numbers
    length = 10
    email = "".join(random.sample(sample, length)) + domain
    print("---------EMAIL & PASSWORD---------")
    print("Your Email is:", email)

genRanEmail()
genRanPassword()

# Encrypting the password
def encryptPassword():
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    ciphered_text = cipher_suite.encrypt(b"Your Password is:")
    print("Ciphered Password:", ciphered_text)
    unciphered_text = cipher_suite.decrypt(ciphered_text)
    print("Deciphered Password:", unciphered_text)

encryptPassword()




