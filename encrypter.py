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
    message = input("What is your message? ")
    spmessage = (split(message)) 
    for ab in range(len(spmessage)):
        spmessage[ab] = str(ord(spmessage[ab]))
    message = "".join(spmessage)
    message = int(message)
    fileName = open("encryptpasswords.txt", "r")
    if fileName.mode == 'r':
        words = fileName.read()
        message = message*2
        print(message)

elif enode == "DECRYPTING":
    typekey = input("Are you decrypting regular key or private key messages.")
    typekey = typekey.upper()

    if typekey == "PRIVATE":
        prvkey = int(input)

elif enode == "CREATING":
    for aa in range(1):
        pubkey = randint(10000,99999)
    prvkey = int((((((((((pubkey+100000)*123)+123)/123)+3)*123)-236)/123)-1)*123)
    for ac in range(1):
        regkey = randint(1000,9999)
    print(pubkey)
    print(prvkey)
    print(regkey)

    fileName = open("C:\Users\krisp\OneDrive - education.wa.edu.au\Year 8\Math\Coding\Project1\Python\passwords.txt", "w+")
    fileName.write(str(pubkey))
    fileName.write(str(prvkey))
    fileName.write(str(regkey))
    fileName.close()