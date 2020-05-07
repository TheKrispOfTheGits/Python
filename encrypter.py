import time
import random

print()
print()
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

