import time
import random
from random import seed
from random import randint

seed(1)
print("Hello")
time.sleep(0.5)
print("I am an encrypter/decrypter.")
time.sleep(0.5)
enode = input("Are you encrypting or decrypting? ")
enode = enode.upper()

if enode == "ENCRYPTING":
    pubkeytrue = input("Do you have a lock? ")
    pubkeytrue = pubkeytrue.upper()

    if pubkeytrue == "YES":
        pubkey = input("What is your lock? ")

    elif pubkeytrue == "NO":
        pubkeyverif = input("Do you want to create a lock? ")
        pubkeyverif = pubkeyverif.upper()
        
        if pubkeyverif == "YES":
            for aa in range(1):
                pubkey = randint(100,999)
            print(f"Your lock is: {pubkey}")
                
        
        
for aa in range(1):
    value = randint(0,94)
    print(value)