import time
import random
from random import seed
from random import randint

def split(message): 
    return [char for char in message]  

global message
seed(1)
print("Hello")
time.sleep(0.5)
print("I am an encrypter/decrypter.")
time.sleep(0.5)
enode = input("Are you encrypting, decrypting or creating? ")
enode = enode.upper()

if enode == "ENCRYPTING":
    pubkey = int(input("What is your lock? "))
    message = input("What is your message? ")
    spmessage = (split(message)) 
    for ab in range(len(spmessage)):
        spmessage[ab] = str(ord(spmessage[ab]))
    message = "".join(spmessage)
    message = int(message)
    message = message*pubkey
    print(message)

elif enode == "CREATING":
    createverif = input("Do you want to create a public lock, private key and regular key? ")
    createverif = createverif.upper()

    if createverif == "YES":
        for aa in range(1):
            pubkey = randint(10000,99999)
        print(f"Your lock is: {pubkey}")
        prvkey = (pubkey+100000)*123
        print(f"Your private key is {prvkey}")
        for ac in range(1):
            regkey = randint(1000,9999)
        print(f"Your regular key is {regkey}")